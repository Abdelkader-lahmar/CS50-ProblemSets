from datetime import date
from seasons import generate_string, calculate_minutes_number, get_date_from_user
from pytest import raises
#the methode of simulating input function took from chatgpt
from unittest.mock import patch


def test_seasons():
    assert generate_string(calculate_minutes_number(date(2000, 1, 1), date(1999, 1, 1))) == "Five hundred twenty-five thousand, six hundred minutes"
    assert generate_string(calculate_minutes_number(date(2003, 1, 1), date(2001, 1, 1))) == "One million, fifty-one thousand, two hundred minutes"
    assert generate_string(calculate_minutes_number(date(2032, 1, 1), date(2020, 6, 1))) == "Six million, ninety-two thousand, six hundred forty minutes"
    with patch("builtins.input", side_effect="hello"):
        raises(SystemExit, get_date_from_user)

