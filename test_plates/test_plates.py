from plates import is_valid


def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("whatsp") == True
    assert is_valid("fd2006") == True


def test_digit_in_middle():
    assert is_valid("cs50x") == False
    assert is_valid("kh85h6") == False


def test_zero_first():
    assert is_valid("Cs05") == False
    assert is_valid("pytho0") == False


def test_range():
    assert is_valid("h") == False
    assert is_valid("hihihih") == False


def test_olny_numbers():
    assert is_valid("2005") == False
    assert is_valid("0534") == False


def test_with_punc():
    assert is_valid("!hi") == False
    assert is_valid("hi,50") == False



