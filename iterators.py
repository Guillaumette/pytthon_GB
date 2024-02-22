data = {"один": 1, "два": 2, "три": 3}
x = iter(data.items())
print("x =", x)
y = next(x)
print("y =", y)
z = next(iter(y))
print("z =", z)