import inflect

names = []
p = inflect.engine()
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break

print(f"\nAdieu, adieu, to {p.join(names)}")
