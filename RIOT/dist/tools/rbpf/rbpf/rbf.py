import struct
import logging
from collections import namedtuple
from elftools.elf.elffile import ELFFile

from rbpf import instructions
import itertools

MAGIC = int.from_bytes(b'rBPF', "little")

HEADER_STRUCT = struct.Struct('<IIIIIIII')
HEADER = namedtuple('Header', 'magic version flags data_len bss_len rodata_len text_len functions_len')

SYMBOL_STRUCT = struct.Struct('<HHH')
SYMBOL = namedtuple('Symbol', 'name_offset flags location_offset')

TEXT = '.text'
DATA = '.data'
BSS = '.bss'
RODATA = '.rodata'
SYMBOLS = '.symtab'
TEXT_RELOCATIONS = '.rel.text'
DATA_RELOCATIONS = '.rel.data'
RODATA_RELOCATIONS = '.rel.rodata'

COMPRESSED = 0x01

# https://docs.kernel.org/bpf/llvm_reloc.html
R_BPF_NONE = 0
R_BPF_64_64 = 1
R_BPF_64_ABS64 = 2
R_BPF_64_ABS32 = 3
R_BPF_64_NODYLD32 = 4
R_BPF_64_32 = 10

BPF_RELOC_TYPE_NAMES = {
    R_BPF_NONE: "R_BPF_NONE",
    R_BPF_64_64: "R_BPF_64_64",
    R_BPF_64_ABS64: "R_BPF_64_ABS64",
    R_BPF_64_ABS32: "R_BPF_64_ABS32",
    R_BPF_64_NODYLD32: "R_BPF_64_NODYLD32",
    R_BPF_64_32: "R_BPF_64_32",
}

class Symbol(object):
    def __init__(self, location, name, instruction=None):
        self.location = location
        self.name = name
        self.instruction = instruction

class RBF(object):


    def __init__(self, data, bss_len, rodata, text, symbols, header=None):
        self.data = data
        self.bss_len = bss_len
        self.rodata = rodata
        self.text = text
        self.header = header
        if header:
            self.flags = self.header.flags
        else:
            self.flags = 0
        self.instructions = instructions.parse_text(self.text, compressed=bool(self.flags & COMPRESSED))
        self.symbols = symbols

        def _round_len(bstr):
            if (len(bstr) % 8) != 0:
                bytes_to_append = 8 - len(bstr) % 8
                logging.debug(f"appending {bytes_to_append} bytes")
                bstr += bytes([0x00] * bytes_to_append)

        _round_len(self.data)
        self.bss_len = bss_len if bss_len % 8 == 0 else bss_len + 8 - bss_len % 8
        _round_len(self.rodata)

        if (len(text) % 8) != 0:
            logging.error(f"Length of the text is not a whole number of instructions: {len(text)}")

    def _parse_symbols(self, symbols):
        syms = []
        for symbol in symbols:
            rodata_offset = symbol.name_offset
            name = self.rodata[rodata_offset:].split(b'\00')[0].decode('ascii')
            instruction = self.instruction_by_address(symbol.location_offset)
            syms.append(Symbol(symbol.location_offset, name, instruction))
        return syms

    def instruction_by_address(self, address):
        for instruction in self.instructions:
            if instruction.address == address:
                return instruction
        return None

    @staticmethod
    def _hex_dump(data):
        return " ".join(map("0x{0:0>2X}".format, data))

    @staticmethod
    def _split_instructions(data):
        iterator = [iter(data)] * 8
        return list(itertools.zip_longest(*iterator))

    @staticmethod
    def obj_hexstr(bstr):
        addr = 0
        while len(bstr) > 0:
            slice_len = 8 if len(bstr) > 8 else len(bstr)
            line = bstr[:slice_len]
            bstr = bstr[slice_len:]
            yield "{:>5x}: ".format(addr) + " ".join(map("0x{0:0>2x}".format, line)) + "\n"
            addr += 8

    def dump(self, compressed=False):
        print(f"Magic:\t\t{hex(self.header.magic)}\n"
              f"Version:\t{self.header.version}\n"
              f"flags:\t{hex(self.flags)}\n"
              f"Data length:\t{self.header.data_len} B\n"
              f"Bss length:\t{self.header.bss_len} B\n"
              f"RoData length:\t{self.header.rodata_len} B\n"
              f"Text length:\t{self.header.text_len} B\n"
              f"No. functions:\t{self.header.functions_len}\n"
              )
        print("functions:")
        syms = {sym.location: sym for sym in self._parse_symbols(self.symbols)}
        for symbol in syms.values():
            print(f"\t\"{symbol.name}\": {hex(symbol.location)}")
        print()

        print("data:")
        print("".join(data for data in RBF.obj_hexstr(self.data)))

        print("rodata:")
        print("".join(data for data in RBF.obj_hexstr(self.rodata)))

        print("text:")
        for instr in self.instructions:
            if compressed:
                print(instr.compressed_print())
            else:
                if instr.address in syms:
                    symbol = syms[instr.address]
                    print(f"<{symbol.name}>")
                print(instr.full_print())

    def format(self):
        if not self.header:
            self.header = HEADER(MAGIC, 0, 0, len(self.data), self.bss_len, len(self.rodata),
                                 len(self.text), len(self.symbols))

        data = bytearray(HEADER_STRUCT.pack(*self.header))
        data += self.data
        data += self.rodata
        data += self.text
        for symbol in self.symbols:
            data += SYMBOL_STRUCT.pack(*symbol)
        return data

    def format_compressed(self):
        compressed_text = bytes().join(instr.compress() for instr in self.instructions)
        if not self.header:
            self.header = HEADER(MAGIC, 0, COMPRESSED, len(self.data), self.bss_len, len(self.rodata),
                                 len(compressed_text), len(self.symbols))
        data = bytearray(HEADER_STRUCT.pack(*self.header))
        data += self.data
        data += self.rodata
        data += compressed_text
        for symbol in self.symbols:
            data += SYMBOL_STRUCT.pack(*symbol)
        return data


    @staticmethod
    def from_rbf(byte_data):
        header = HEADER._make(HEADER_STRUCT.unpack_from(byte_data, 0))
        offset = HEADER_STRUCT.size
        data_start = offset
        offset += header.data_len
        data_end = offset
        bss_len = header.bss_len
        rodata_start = offset
        offset += header.rodata_len
        text_start = rodata_end = offset
        offset += header.text_len
        syms_start = text_end = offset
        rodata = byte_data[rodata_start:rodata_end]
        data = byte_data[data_start:data_end]
        text = byte_data[text_start:text_end]
        syms = byte_data[syms_start:]

        syms_array = []
        while len(syms):
            syms_array.append(
                SYMBOL._make(SYMBOL_STRUCT.unpack_from(syms, 0))
            )
            syms = syms[SYMBOL_STRUCT.size:]
        return RBF(data, bss_len, rodata, text, syms_array, header)


    @staticmethod
    def _get_section_lddw_opcode(section):
        if section.startswith(RODATA):
            return instructions.LDDWR_OPCODE
        elif section.startswith(DATA):
            return instructions.LDDWD_OPCODE
        elif section.startswith(BSS):
            return instructions.LDDWB_OPCODE
        else:
            raise ValueError(f"Relocation in unsupported section: {section}")

    @staticmethod
    def _patch_text(text, elffile, relocation, intersection_offset):
        entry = relocation.entry
        location = entry.r_offset
        symbol = elffile.get_section_by_name(SYMBOLS).get_symbol(entry.r_info_sym)

        r_type = symbol.entry.st_info.type
        if r_type == 'STT_SECTION' or r_type == 'STT_OBJECT':
            section_name = elffile.get_section(symbol.entry.st_shndx).name
            offset = symbol.entry.st_value
            is_offset = intersection_offset[section_name]
            if is_offset > 0:
                logging.info(f"Symbol was located in a merged section. Applying inter-section offset {is_offset}")
            offset += is_offset
            opcode = RBF._get_section_lddw_opcode(section_name)
            if text[location] != instructions.LDDW_OPCODE:
                raise ValueError(f"No LDDW instruction at {hex(location)}")
            inst = instructions.LDDW._make(instructions.LDDW_STRUCT.unpack_from(text, location))
            logging.info(f"Patching {inst} at 0x{location:x} with new opcode 0x{opcode:x} and target 0x{offset:x}")
            patched_inst = instructions.LDDW_STRUCT.pack(
                opcode,
                inst.registers,
                inst.offset,
                inst.immediate_l + offset,
                0,
                0,
                0,
                inst.immediate_h
            )
        elif r_type == 'STT_NOTYPE':
            return
        elif r_type == 'STT_FUNC':
            byte_offset = symbol.entry.st_value - location
            imm, rem = divmod(byte_offset, 8)
            imm -= 1 # The instruction index points to the next instruction already
            opcode = instructions.Call_OPCODE
            if text[location] != opcode:
                raise ValueError(f"No CALL instruction at {hex(location)}")
            inst = instructions.CALL._make(instructions.CALL_STRUCT.unpack_from(text, location))
            logging.info(f"Patching {inst} at 0x{location:x} with new opcode 0x{opcode:x} and target 0x{symbol.entry.st_value:x}")
            patched_inst = instructions.CALL_STRUCT.pack(
                opcode,
                inst.registers,
                inst.offset,
                imm
            )
            assert rem == 0
        else:
            raise ValueError(f"Unknown st_info {symbol.entry.st_info.type}")

        assert patched_inst is not None

        text[location:location + len(patched_inst)] = patched_inst


    @staticmethod
    def from_elf(elf, relocations=True):
        elffile = ELFFile(elf)
        text_relocations = elffile.get_section_by_name(TEXT_RELOCATIONS)
        data_relocations = elffile.get_section_by_name(DATA_RELOCATIONS)
        rodata_relocations = elffile.get_section_by_name(RODATA_RELOCATIONS)

        bss_len = 0

        elf_sections = {
            TEXT: [],
            RODATA: [],
            DATA: [],
        }

        data = {
            TEXT: bytearray(),
            RODATA: bytearray(),
            DATA: bytearray(),
        }

        # The bss section is zeroed. We only tack its length.
        intersection_offset = { BSS: 0 }

        for section in elffile.iter_sections():
            logging.info(f"Processing {section.name}")
            if section.name.startswith(TEXT):
                elf_sections[TEXT].append(section)
            elif section.name.startswith(DATA):
                elf_sections[DATA].append(section)
            elif section.name.startswith(BSS):
                if bss_len != 0:
                    raise ValueError(f"Merging {section.name} into {bss_len} BSS not supported")
                bss_len = section.data_size
            elif section.name.startswith(RODATA):
                elf_sections[RODATA].append(section)

        for c in [TEXT, RODATA, DATA]:
            if elf_sections[c]:
                str_sections = ", ".join(["\"" + x.name + "\"" for x in elf_sections[c]])
                logging.info(f"Merging {len(elf_sections[c])} section(s) into {c}: [{str_sections}]")
                for section in elf_sections[c]:
                    intersection_offset[section.name] = len(data[c])
                    data[c] += section.data()

        symbols = elffile.get_section_by_name(SYMBOLS)

        rbf_symbols = []
        for symbol in symbols.iter_symbols():
            entry = symbol.entry
            info = entry['st_info']
            if info['type'] == 'STT_FUNC' and info['bind'] == 'STB_GLOBAL':
                name = symbol.name
                text_offset = entry['st_value']
                logging.info(f"Found global function {name} at offset {text_offset}")
                rbf_symbols.append((name, text_offset, 0)) # potential flags

        symbol_structs = []
        logging.debug(f"rodata length: {len(data[RODATA])}")
        for name, text_offset, flags in rbf_symbols:
            offset = len(data[RODATA])
            data[RODATA] += bytes(name, 'UTF-8') + b'\00'
            sym_str = SYMBOL(offset, flags, text_offset)
            symbol_structs.append(sym_str)
            logging.debug(f"symbol {sym_str} generated with {name} and appended at {offset}")
        logging.info(f"Total rodata size: {len(data[RODATA])}. Total data size: {len(data[DATA])}")

        if relocations:
            for relocation in text_relocations.iter_relocations() if text_relocations else []:
                entry = relocation.entry
                symbol = symbols.get_symbol(entry['r_info_sym'])
                symbol_type = symbol['st_info'].type
                rel_type = BPF_RELOC_TYPE_NAMES[entry['r_info_type']]
                target_section = elffile.get_section(symbol.entry['st_shndx'])


                # logging.info(f"Relocation ({rel_type}) of {symbol.name} (type {symbol_type}). Instruction at {hex(entry['r_offset'])} accesses {target_section.name} + {symbol.entry.st_value}")
                if rel_type not in  ['R_BPF_64_64', 'R_BPF_64_32']:
                    raise ValueError(f"Unsupported relocation type {rel_type}")

                RBF._patch_text(data[TEXT], elffile, relocation, intersection_offset)

            if data_relocations is not None and data_relocations.num_relocations() > 0:
                for relocation in data_relocations.iter_relocations():
                    name = symbols.get_symbol(relocation.entry['r_info_sym']).name
                    logging.critical(f"{symbols.get_symbol(relocation.entry['r_info_sym']).name} requires a relocation in the data section!")
                raise ValueError(f"Relocating values in the data section are not supported!")

            if rodata_relocations is not None and rodata_relocations.num_relocations() > 0:
                for relocation in rodata_relocations.iter_relocations():
                    logging.critical(f"{symbols.get_symbol(relocation.entry['r_info_sym']).name} requires a relocation in the rodata section!")
                raise ValueError(f"Relocating values in the rodata section are not supported!")
        return RBF(data=data[DATA], bss_len=bss_len, rodata=data[RODATA], text=data[TEXT], symbols=symbol_structs)
