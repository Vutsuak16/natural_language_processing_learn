k = [1, 2, 3, 4, 5]
l = [1, 4, 9, 16, 25]
m = [1, 8, 64, 125, 216]

lamb = lambda x, y: x + y
for i in range(5):
    print(lamb(k[i], l[i]), end=" ")

print("\n")

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9) / 5) * x + 32, Celsius)
for i in Fahrenheit:
    print(i,end=" ")