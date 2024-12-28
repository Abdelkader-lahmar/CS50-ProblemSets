from datetime import date
import inflect
import re
import sys


def main():
    print(generate_string(calculate_minutes_number(date.today(), get_date_from_user())))


def get_date_from_user():
    return is_valid(re.search(r"^(\d{4})-([01]\d)-([0-3]\d)$", input("Date of Birth: ")))


def is_valid(day):
    if not day:
        sys.exit("Invalid date")
    return date(int(day.group(1)), int(day.group(2)), int(day.group(3)))


def calculate_days_number(first, second):
    return (first - second).days


def calculate_minutes_number(first, second):
    return calculate_days_number(first, second) * 24 * 60


def generate_string(number):
    return inflect.engine().number_to_words(number, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()
