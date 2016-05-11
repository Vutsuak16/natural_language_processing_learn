def count_percentage(count, total):
    return (100 * count / total)


text = ["Radhe", "ne", "ek", "baar", "committment", "kardi", "toh", "woh", "apni", "bhi", "nhi", "sunta", "Radhe", "is",
        "cool", "be", "like", "Radhe"]

print(count_percentage(text.count("Radhe"), len(text)))
