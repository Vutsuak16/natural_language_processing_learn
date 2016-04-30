from itertools import islice

l = ["kaustuv", "is", "a", "good", "boy"]
k = []
try:
    for i in range(len(l)):
        x = (l[i - 1], l[i])
        k.append(x)
except:
    pass

print(k)