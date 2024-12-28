import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if " to " not in s:
        raise ValueError
    first, second = s.split(" to ")
    return f"{handle(first)} to {handle(second)}"


def handle(time):
    if not (time := re.search(r"^([01]?\d)(?::([0-5]\d))? ([AP]M)$", time)):
        raise ValueError
    hours, minute = int(time.group(1)), time.group(2)
    if not minute:
        minute = 0
    else:
        minute = int(minute)
    if not 0 <= minute <= 59 or not 0 <= hours <= 12:
        raise ValueError
    match (hours, time.group(3)):
        case (12, "PM"):
            hours = 12
        case (12, "AM"):
            hours = 0
        case (hours, "PM"):
            hours += 12
    return f"{hours:02}:{minute:02}"


if __name__ == "__main__":
    main()
