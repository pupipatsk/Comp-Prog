a = float(input())
b = float(input())
c = float(input())

x1 = round( (-b - (b**2 - 4*a*c)**.5) / (2*a), 3)
x2 = round( (-b + (b**2 - 4*a*c)**.5) / (2*a), 3)

print(x1, x2)