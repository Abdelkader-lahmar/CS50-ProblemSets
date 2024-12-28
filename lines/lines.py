import sys


def main():
    command_line_check = check_command_line(sys.argv)
    if command_line_check != "ok":
        sys.exit(command_line_check)
    else:
        print(calculate_lines(sys.argv[1]))


def check_command_line(argv):
    if len(argv) < 2:
        return "Too few command-line arguments"
    elif len(argv) > 2:
        return "Too many command-line arguments"
    elif not argv[1].endswith(".py"):
        return "Not a Python file"
    else:
        try:
            with open(argv[1], "r") as program:
                return "ok"
        except FileNotFoundError:
            return "File does not exist"


def calculate_lines(program_name):
    number = 0
    with open(program_name, "r") as program:
        for line in program:
            if line.lstrip().startswith("#") or line.isspace():
                continue
            else:
                number += 1
    return number


if __name__ == "__main__":
    main()
