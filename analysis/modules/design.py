import matplotlib.pyplot as plt
import numpy as np
from colour import Color
from textwrap import wrap, fill
from typing import List
import matplotlib.ticker as ticker

#bc_palette = {
#    "jerryscript": "#FFD166",
#    "micropython": "#0CB082",
#    "lua": "#118AB2",
#    "wamr": "#C98DCA",
#    "wamr-fast": "#BF6EF2",
#    "micro-bpf": "#9E5454",
#    #"aot": "#CF2A39",
#    "native": "#073B4C"
#}

bc_palette = {
    "JerryScript": "#E6AB02",
    "MicroPython": "#66A61E",
    "Lua": "#7570B3",
    "WAMR": "#A6761E",
    "WAMR (fast)": "#D95F02",
    "µBPF": "#E7298A",
    #"aot": "#1B9E77",
    "Native": "#666666"
}

b_order = ["mont64", "sha256", "md5", "crc_32", "ud", "xgboost", "tarfind", "huffbench", "statemate", "matmult-int", "nsichneu", "slre"]
b_cat = ["Pure Compute", "Mostly Compute", "Balanced", "Branching", "Memory", "Branching + Memory"]

def lighter(c):
    tmp = Color(c)
    tmp.set_luminance(max(0, tmp.get_luminance() + 0.1))
    return tmp.hex

def darker(c):
    tmp = Color(c)
    tmp.set_luminance(max(0, tmp.get_luminance() - 0.1))
    return tmp.hex

def lightest(c):
    return lighter(lighter(c))

def darkest(c):
    return darker(darker(c))

def set_hatch(ax: plt.Axes, known_patches, hatch, linewidth: float= 0.75, color:str = "black"):
    for bar in set(ax.patches) - known_patches:
        bar.set_hatch(hatch)
        bar.set_hatch_linewidth(linewidth)
        bar.set_edgecolor(color)
    known_patches.update(ax.patches)


def wrap_and_center(s: List[str], l: int) -> List[str]:
    res = []
    for elem in s:
        res.append(fill("\n".join([line.center(l) for line in wrap(elem, l)]), l))
    return res

def set_yticks(ax: plt.Axes, step: int, minor_step: int | None = None, both_sides: bool = False, start_offset:int = 0) -> None:
    mi, ma = ax.get_ylim()
    steps = np.arange(mi, ma + 1, step)
    ax.set_yticks(steps[steps >= start_offset])
    ax.tick_params(axis="y", which="major", right=False, length=6, width=1)
    for tick in ax.yaxis.get_major_ticks():
        tick.tick1line.set_visible(True)
        tick.tick2line.set_visible(both_sides)
    if minor_step is None:
        return
    ax.minorticks_on()
    ax.tick_params(axis="y", which="minor", right=False, length=3, width=1)
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(minor_step))
    for tick in ax.yaxis.get_minor_ticks():
        tick.tick1line.set_visible(True)
        tick.tick2line.set_visible(both_sides)

def set_frame(ax: plt.Axes, color: str = "black", linewidth: float =1.0):
    for s in ax.spines.values():
        s.set_edgecolor(color)
        s.set_linewidth(linewidth)
