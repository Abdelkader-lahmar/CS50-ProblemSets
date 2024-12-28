import csv
import sys


def main():
    command_line_check = check_command_line(sys.argv)
    if command_line_check != "ok":
        sys.exit(command_line_check)
    students = read_csv(sys.argv[1])
    students = fix_names(students)
    write_csv(sys.argv[2], students)


def write_csv(file_name, content):
    with open(file_name, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in content:
            writer.writerow(row)


def fix_names(students):
    for student in students:
        last, first = student["name"].split(",")
        student["last"], student["first"] = last.lstrip(), first.lstrip()
        del student["name"]
    return students


def read_csv(file_name):
    rows = []
    with open(file_name, "r") as file:
        for row in csv.DictReader(file):
            rows.append(row)
    return rows


def check_command_line(argv):
    if len(argv) < 3:
        return "Too few command-line arguments"
    elif len(argv) > 3:
        return "Too many command-line arguments"
    elif not argv[1].endswith(".csv") or not argv[2].endswith(".csv"):
        return "Not a CSV file"
    else:
        try:
            with open(argv[1], "r") as program:
                return "ok"
        except FileNotFoundError:
            return "File does not exist"


if __name__ == "__main__":
    main()
