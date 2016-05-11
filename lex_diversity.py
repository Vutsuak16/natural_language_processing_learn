def lex_div(text):
    return len(text) / len(set(text))


print(lex_div(
    ["Radhe", "ne", "ek", "baar", "committment", "kardi", "toh", "woh", "apni", "bhi", "nhi", "sunta", "Radhe", "is",
     "cool", "be", "like", "Radhe"]))
