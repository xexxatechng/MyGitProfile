"""
Permutation P is given as (nPr = n!/(n! - r!))  where n! = n Factorial and r! = r factorial
"""
import math
#Enter value for permutation

n_value = int(input("Enter value for n: "))
r_value = int(input("Enter value for r: "))
n_factorial = math.factorial(n_value)
print(n_factorial)
print()
print("Let k_constant = (n_value - r_value)")
k_constant = n_value - r_value
k_factorial = math.factorial(k_constant)
print(k_factorial)
print()
permutation = n_factorial / k_factorial
print("nPk: = " + str(permutation))
