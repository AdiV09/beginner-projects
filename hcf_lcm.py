import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

lcm = math.lcm(a, b)
hcf = math.gcd(a, b)

print(f"LCM: {lcm}\nHCF: {hcf}")
