import csv
import sys
from tabulate import tabulate


def main():
    command_line_check = check_command_line(sys.argv)
    if command_line_check != "ok":
        sys.exit(command_line_check)
    table = read_csv(sys.argv[1])
    print(tabulate(table, headers="keys", tablefmt="grid"))


def check_command_line(argv):
    if len(argv) < 2:
        return "Too few command-line arguments"
    elif len(argv) > 2:
        return "Too many command-line arguments"
    elif not argv[1].endswith(".csv"):
        return "Not a CSV file"
    else:
        try:
            with open(argv[1], "r") as program:
                return "ok"
        except FileNotFoundError:
            return "File does not exist"


def read_csv(file_name):
    rows = []
    with open(file_name, "r") as file:
        for row in csv.DictReader(file):
            rows.append(row)
    return rows


if __name__ == "__main__":
    main()
