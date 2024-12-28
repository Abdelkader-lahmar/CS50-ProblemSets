from fuel import convert, gauge
import pytest


def test_valid_per():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99


def test_exception():
    pytest.raises(ValueError, convert, "three/two")
    pytest.raises(ValueError, convert, "5-5")
    pytest.raises(ValueError, convert, "1.5/3")
    pytest.raises(ValueError, convert, "2/3.4")
    pytest.raises(ZeroDivisionError, convert, "1/0")


def test_E():
    assert gauge(1) == "E"
    assert gauge(0.5) == "E"


def test_F():
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_middle():
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
