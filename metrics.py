from nltk.metrics import *

print(edit_distance("kaustuv", "kaustuv boy"))  # levenshtein distance

s1 = set([1, 2, 3])
s2 = set([3, 4, 5, 5, 6, 7])

print(binary_distance(s1, s2))

# what is binary distance??

print(jaccard_distance(s1, s2))

print(masi_distance(s1, s2))
