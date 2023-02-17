from math import tan, pi
n = int(input("Input number of sides: "))
l = float(input("Input the length of a side: "))
A = n * (l ** 2) / (4 * tan(pi / n))
print("The area of the polygon is: ", A)