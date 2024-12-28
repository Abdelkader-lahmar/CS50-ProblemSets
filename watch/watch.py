import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if not (url := re.search(r'src="https?://(?:www\.)?youtube.com/embed/(\w+)"', s)) or not url.group(1):
        return None
    return f"https://youtu.be/{url.group(1)}"


if __name__ == "__main__":
    main()
