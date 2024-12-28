text = input("Input: ")
for c in text:
    if c.lower() not in ["a", "e", "i", "o", "u"]:
        print(c, end="")
print()
