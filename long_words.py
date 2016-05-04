f=open("calculus.txt")
s=f.read()
s=s.split(" ")
lw=[l for l in s if len(l)>10]
print(lw)