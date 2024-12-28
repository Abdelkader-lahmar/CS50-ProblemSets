from cs50 import get_int

height = get_int("Height: ")

while height < 1 or height > 8:
    height = get_int("Height: ")


def print_row(lenght):
    for i in range(lenght):
        print('#', end="")


def print_void(lenght):
    for i in range(lenght):
        print(" ", end="")


for i in range(height):
    print_void(height - i - 1)
    print_row(i + 1)
    print("")
