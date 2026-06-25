// SPDX-FileCopyrightText: 2020 Christian Amsüss
// SPDX-License-Identifier: LGPL-2.1-only
#![no_std]

mod infra;
mod middleware;
mod util;

use core::error::Error;
use core::{panic, usize};

use alloc::string::ToString;
use rbpf::EbpfVmMbuff;
use rbpf::lib::format;
use riot_wrappers::ztimer::{Clock, Ticks};
use riot_wrappers::{println, riot_main};

extern crate alloc;
extern crate riot_sys;
extern crate rust_riotmodules;

use alloc::vec::Vec;
use alloc::vec;
use alloc::collections::BTreeMap;
use alloc::boxed::Box;

use crate::middleware::helpers::register_all;

use log::{Record, Level, Metadata, SetLoggerError, LevelFilter, debug};

const fn parse_usize(s: &str)-> usize {
    let mut out:usize = 0;
    let mut i:usize = 0;
    while i<s.len() {
        out *= 10;
        out += (s.as_bytes()[i] - b'0') as usize;
        i += 1;
    }
    out
}

#[macro_export]
macro_rules! print {
    ( $( $arg:expr ),* ) => {{
        use core::fmt::Write;
        use riot_wrappers::stdio::Stdio;
        let _ = write!(Stdio {}, $( $arg, )* );
    }}
}

riot_main!(main);

const ITERATIONS_STR: &str = env!("ITERATIONS");

#[cfg(feature = "jit")]
#[repr(C, align(4))]
struct AlignedBuffer([u8; JIT_MEMORY_BUFF_SIZE]);

#[cfg(feature = "jit")]
const JIT_MEMORY_BUFF_SIZE: usize = 2 << 16;

#[cfg(not(feature = "jit"))]
#[repr(align(4))]
struct EBPFByteCodeBuffer{ app: [u8; include_bytes!("../benchmark.bin").len()]}

struct RiotLogger;

impl log::Log for RiotLogger {
    fn enabled(&self, metadata: &Metadata) -> bool {
        metadata.level() <= Level::Debug
    }

    fn log(&self, record: &Record) {
        if self.enabled(record.metadata()) {
            riot_wrappers::println!("{} - {}", record.level(), record.args());
        }
    }

    fn flush(&self) {}
}

static LOGGER: RiotLogger = RiotLogger;

pub fn init() -> Result<(), SetLoggerError> {
    log::set_logger(&LOGGER)
        .map(|()| log::set_max_level(LevelFilter::Debug))
}


#[cfg(feature = "measure_malloc")]
pub fn get_malloc_high() -> usize {
   return  unsafe {riot_sys::malloc_monitor_get_usage_high_watermark() as usize}
}

fn main() {

    #[cfg(feature = "jit")]
    static APP: EBPFByteCodeBuffer = EBPFByteCodeBuffer{app: *include_bytes!("../benchmark.o")};

    #[cfg(not(feature = "jit"))]
    static APP: EBPFByteCodeBuffer = EBPFByteCodeBuffer{app: *include_bytes!("../benchmark.bin")};

    let prog: &[u8] = &APP.app;

    let micro_sec = Clock::usec();
    let iterations: usize = ITERATIONS_STR.parse().expect("Failed to parse ITERATIONS");

    // Sleep a bit to wait for the serial to be ready
    micro_sec.sleep(Ticks::from_duration(core::time::Duration::from_secs(3)).
            expect("5 would only overflow a nanosecond timer"));
    #[cfg(feature = "measure_malloc")]
    let before: usize = get_malloc_high();
    println!("=== Benchmark Begins ===");
    println!("iteration;init_runtime_us;load_program_us;execution_time_us;correct");

    for i in 0..iterations {
        print!("{};", i);
        print!("0;"); // init runtime not applicable here

        let mut vm: Option<EbpfVmMbuff> = None;

        #[cfg(feature = "jit")]
        let mut jitted_fn: Option<unsafe fn(*mut u8, usize, *mut u8, usize) -> u32> = None;

        #[cfg(feature = "jit")]
        let mut jit_memory_buff: Box<AlignedBuffer> = Box::new(AlignedBuffer([0; JIT_MEMORY_BUFF_SIZE]));

        debug!("Loading...");
        let load_program_duration = micro_sec
            .time(|| {
                #[cfg(not(feature = "jit"))]
                {
                    vm = Some(
                        EbpfVmMbuff::new(Some(prog), rbpf::InterpreterVariant::FemtoContainersHeader)
                            .expect("failed to load program"),
                    );
                    register_all(vm.as_mut().unwrap());
                    debug!("Verifying...");
                    vm.as_ref().unwrap().verify_loaded_program().expect("program verification failed");
                }

                #[cfg(feature = "jit")]
                {
                    use crate::middleware::ALL_HELPERS;

                    let mut prog_vec = prog.to_vec();

                    let mut helpers_map = BTreeMap::new();
                    for h in ALL_HELPERS.iter() {
                        helpers_map.insert(h.id as u32, h.function);
                    }

                    let offset;

                    {
                        let jit = rbpf::JitMemory::new(
                            &mut prog_vec,
                            &mut jit_memory_buff.0,
                            &helpers_map,
                            false,
                            false,
                            rbpf::InterpreterVariant::RawObjectFile
                        ).expect("Failed jit compile");


                        offset = jit.text_offset.clone();
                    }

                    jitted_fn = Some(rbpf::JitMemory::get_prog_from_slice(
                        &jit_memory_buff.0,
                        offset,
                    ));

                    debug!("JIT compilation done.");
                }
            })
            .expect("failed to measure load program time");

        print!("{};", load_program_duration.0);

        let mut res = 0;

        debug!("Executing...");
        let execution_duration = micro_sec
            .time(|| {
                #[cfg(not(feature = "jit"))]
                {
                    let vm = vm.unwrap();
                    let allowed_memory_regions: Vec<(u64, u64)> = Vec::new();

                    res = vm
                        .execute_program(&[], &[], allowed_memory_regions)
                        .expect("programm execution failed");

                }

                #[cfg(feature = "jit")]
                {
                    debug!("Executing JITted code");
                    // Sleep is needed sometimes, because when the execution fails no output is displayed otherwise.
                    // micro_sec.sleep(Ticks::from_duration(core::time::Duration::from_secs(3)).
                    //     expect("5 would only overflow a nanosecond timer"));

                    let start = mem.as_mut_ptr();
                    let end = unsafe { start.add(mem.len()) }; // one-past-the-end

                    debug!("Mem: {:p} - {:p}", start, end);
                    res = unsafe {
                        jitted_fn.unwrap()(0 as *mut u8, 0, mem.as_mut_ptr() as *mut u8, mem.len())
                    };

                    debug!("JITted code execution done.");
                }
            })
            .expect("failed to measure execution time");

        print!("{};", execution_duration.0);
        print!("{}\n", res == 1);
    }

    #[cfg(feature = "measure_malloc")]
    {
        let after: usize = get_malloc_high();
        println!("Dynamically allocated memory: {}", after - before);
    }
    println!("=== Benchmark End ===");
}
