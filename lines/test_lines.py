from lines import check_command_line, calculate_lines


def test_check_command_line():
    assert check_command_line(["lines.py"]) == "Too few command-line arguments"
    assert check_command_line(["lines.py", "program.py", "nothing"]) == "Too many command-line arguments"
    assert check_command_line(["lines.py", "program"]) == "Not a Python file"
    assert check_command_line(["lines.py", "non_existent_file.py"]) == "File does not exist" #Assuming "non_existent_file.py" doesn’t exist
    assert check_command_line(["lines.py", "lines.py"]) == "ok"

def test_calculate_lines():
    assert calculate_lines("file1.py") == 2
    assert calculate_lines("file2.py") == 5
    assert calculate_lines("file3.py") == 5
    assert calculate_lines("file4.py") == 6
