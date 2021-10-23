from Machine import *

rule = {
    "A0": ("B", "0", "R"),
    "A1": ("B", "1", "R"),
    "B0": ("C", "0", "R"),
    "B1": ("A", "0", "L"),
    "C0": ("B", "1", "S"),
    "C1": ("D", "0", "L"),
}
Machine1 = TuringMachine(rule)

Machine1.do_calculation([1, 0, 0, 0, 0, 1])
