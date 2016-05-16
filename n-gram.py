
l = ["kaustuv", "is", "a", "good", "boy", "code", "is", "life", "hi", "guys", "jai", "hanuman"]
k = []
n = 3
try:
    for i in range(0, len(l)):
        x = []
        for j in range(i, n + i):
            x.append(l[j])
        k.append(x)
except:
    pass

print(k)
