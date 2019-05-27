"""
Permutation P is given as (nCr = n!/(n! - r!)r!)  where n! = n Factorial and r! = r factorial
"""
import math
#Enter value for combination

n_value = int(input("Enter value for n: "))
r_value = int(input("Enter value for r: "))
n_factorial = math.factorial(n_value)
print(n_factorial)
print()
r_factorial = math.factorial(r_value)
print()
print("Let k_constant = (n_value - r_value)")
k_constant = n_value - r_value
k_factorial = math.factorial(k_constant)
print(k_factorial)
print()
combination = n_factorial / (k_factorial*r_factorial)
print("nPk: = " + str(combination))
