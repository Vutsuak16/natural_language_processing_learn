k = [1, 2, 3, 4, 5]
l = [1, 4, 9, 16, 25]
m = [1, 8, 64, 125, 216]
lower = ['a', 'b', 'c']
upper = ['A', 'B', 'C']

lamb = lambda x, y: x + y
for i in range(5):
    print(lamb(k[i], l[i]), end=" ")

print("\n")

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9) / 5) * x + 32, Celsius)
for i in Fahrenheit:
    print(i, end=" ")

print("\n")

filtered = filter(lambda x: x % 2 == 0, m)
for i in filtered:
    print(i, end=" ")

print("\n")

# no reduce in python 3 use functools.reduce

to_lower = map(lambda x: x.lower(), upper)

for i in to_lower:
    print(i, end=" ")

print("\n")

to_upper = map(lambda x: x.upper(), lower)

for i in to_upper:
    print(i, end=" ")

print("\n")
