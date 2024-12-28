def main():
    fraction = get_fraction("Fraction: ")
    if 1 < fraction < 99:
        print(f"{fraction}%")
    elif fraction >= 99:
        print("F")
    else:
        print("E")

def get_fraction(promt):
    while True:
        try:
            x, y = input(promt).split("/")
            x, y = int(x), int(y)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if x <= y:
                return round((x / y) * 100)


if __name__ == "__main__":
    main()
