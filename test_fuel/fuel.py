def main():
    while True:
        try:
            percentage = convert(input("Input: "))
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    try:
        x, y = int(x), int(y)
    except ValueError:
        raise ValueError
    else:
        if y == 0:
            raise ZeroDivisionError
        elif x > y or x < 0 or y < 0:
            raise ValueError
        else:
            return round(x / y * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
