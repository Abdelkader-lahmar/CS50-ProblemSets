from numb3rs import validate


def test_valid_ip():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("127.0.0.1") == True
    assert validate("44.215.101.158") == True


def test_invalid_ip():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("255.255.255") == False
    assert validate("275.3.6.28") == False
    assert validate("44.215.101.158.0") == False
    assert validate("25.556.556.556") == False
