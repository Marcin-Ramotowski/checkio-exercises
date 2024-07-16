#!/usr/bin/env checkio --domain=py run write-quadratic-equation

# Quadratic Equationmay be expressed as a product
# a(x-x1)(x-x2) = 0,wherex1andx2are the solutions of equation, so called roots.    After opening the brackets you receive well known form
# a*x**2 + b*x + c = 0.This is what you should do in this mission. You have input list with    integers -a, x1 [, x2]. If it has length 2, it means,x1 == x2: equation    has two equal roots (one distinct root). Your function should return quadratic equation as a string.    Pay attention to specific cases. UseQuadratic Formula Calculatorfor recheck. Good luck!
# 
# Input:List with 2-3 integers.
# 
# Output:String.
# 
# Examples:
# 
# assert quadr_equation([2, 4, 6]) == "2*x**2 - 20*x + 48 = 0"
# assert quadr_equation([-2, 4, 6]) == "-2*x**2 + 20*x - 48 = 0"
# assert quadr_equation([2, 4, -4]) == "2*x**2 - 32 = 0"
# assert quadr_equation([2, 4, 0]) == "2*x**2 - 8*x = 0"
# Preconditions:a != 0; abs(a) == 1 -> '[-]x**2'; a != abs(1) - > '[-]a*x**2'
# exactly one whitespace around signs: [-]a*x**2 sign b*x sign c = 0
# abs(b) == 1 -> [-]a*x**2 sign x sign c = 0
# keep correct view and spacing when x1=x2=0, x1 or x2 = 0, x1=-x2
# 
# 
# END_DESC

def quadr_equation(data: list[int]) -> str:
    if len(data) == 3:
        a, x1, x2 = data
    elif len(data) == 2:
        a, x1 = data
        x2 = x1
    else:
        raise ValueError(f'wrong number of values (expected 2 or 3 got {len(data)})')
    b = -a*x1 - a*x2
    c = a*x1*x2
    text_a = f"{'-' if a < 0 else ''}{f'{abs(a)}*' if abs(a)!= 1 else ''}x**2 "
    text_b = f"{'-' if b < 0 else '+'} {f'{abs(b)}*' if abs(b)!= 1 else ''}x " if b != 0 else ''
    text_c = '= 0' if not c else f"{'+' if c >= 0 else '-'} {abs(c)} = 0"
    return text_a + text_b + text_c


print("Example:")
print(quadr_equation([2, 4, 6]))

assert quadr_equation([2, 4, 6]) == "2*x**2 - 20*x + 48 = 0"
assert quadr_equation([-2, 4, 6]) == "-2*x**2 + 20*x - 48 = 0"
assert quadr_equation([2, 4, -4]) == "2*x**2 - 32 = 0"
assert quadr_equation([2, 4, 0]) == "2*x**2 - 8*x = 0"
assert quadr_equation([2, 0]) == "2*x**2 = 0"
assert quadr_equation([2, 4]) == "2*x**2 - 16*x + 32 = 0"

print("The mission is done! Click 'Check Solution' to earn rewards!")