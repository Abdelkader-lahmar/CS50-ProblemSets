import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not (result := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)):
        return False
    for part in result.groups():
        if not 0 <= int(part) <= 255:
            return False
    return True


if __name__ == "__main__":
    main()
