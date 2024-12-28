grocery = {}
while True:
    try:
        item = input().strip().upper()
    except EOFError:
        items = sorted(grocery)
        for item in items:
            print(f"{grocery[item]} {item}")
        break
    else:
        try:
            grocery[item] += 1
        except KeyError:
            grocery[item] = 1
