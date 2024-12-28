import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)
        for _ in range(4):
            if _ == 3:
                print(f"{x} + {y} = {x + y}")
                break
            try:
                if (x + y) == int(input(f"{x} + {y} = ")):
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 1 <= level <= 3:
                return level


def generate_integer(level):
    match level:
        case  1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)
        case _:
            raise ValueError


if __name__ == "__main__":
    main()
