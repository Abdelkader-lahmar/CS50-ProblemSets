from random import randint


def main():
    while True:
        level = get_int("Level: ")
        if level > 0:
            break

    number = randint(1, level)
    while True:
        guess = get_int("Guess: ")
        if guess < 0:
            continue
        elif guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")
        else:
            print("Just right!")
            break


def get_int(promt):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            pass


if __name__ == "__main__":
    main()
