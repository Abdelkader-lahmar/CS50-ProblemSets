import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    Ums = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(Ums)


if __name__ == "__main__":
    main()
