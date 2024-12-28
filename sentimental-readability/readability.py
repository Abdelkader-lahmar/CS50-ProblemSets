from cs50 import get_string
from string import ascii_letters


def main():
    text = get_string("Text: ")
    level = calcul(text)
    if level > 16:
        print("Grade 16+")
    elif level < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {level}")


def calcul(text):
    words = len(text.split())
    letters = 0
    sentences = 0
    for i in range(len(text)):
        if text[i] in ascii_letters:
            letters += 1
        elif text[i] in ['.', '?', '!']:
            sentences += 1
    return round(0.0588 * (letters / words * 100) - 0.296 * (sentences / words * 100) - 15.8)


main()
