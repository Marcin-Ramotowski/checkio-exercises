#!/usr/bin/env checkio --domain=py run chemical-analysis

# As the input you'll get a chemicalformulaand a numberlimit. Your task is to create a sequence of chemical elements, which are in the amount of>= limitin the formula.
# 
# Pay attention, that in some formulas brackets(), []will be used. They have different meaning in chemistry, but from the point of calculating number of atoms they both work the same way - as ordinary parenthesis in mathematical expression.This articlewill help you to open the brackets and don't make mistakes while counting.
# 
# 
# 
# Input:Chemical formula as string(str)and the limit number of atoms as integer(int).
# 
# Output:Listof certain chemical elements, sorted in the alphabetical order.
# 
# Precondition:
# 1 <= different elements <= 10.
# 
# 
# END_DESC

def atoms(formula: str, limit: int) -> list[str]:
    # replace this for solution
    return []


print("Example:")
print(atoms("C2H5OH", 2))

# These "asserts" are used for self-checking
assert atoms("C2H5OH", 2) == ["C", "H"]
assert atoms("H2O", 2) == ["H"]
assert atoms("Mg(OH)2", 1) == ["H", "Mg", "O"]
assert atoms("K4[ON(SO3)2]2", 4) == ["K", "O", "S"]

print("The mission is done! Click 'Check Solution' to earn rewards!")