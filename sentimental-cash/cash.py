from cs50 import get_float

while True:
    change = get_float("Change: ")
    if change >= 0:
        break

counter = 0
change *= 100
while change >= 25:
    change -= 25
    counter += 1

while change >= 10:
    change -= 10
    counter += 1

while change >= 5:
    change -= 5
    counter += 1

while change > 0:
    change -= 1
    counter += 1

print(counter)
