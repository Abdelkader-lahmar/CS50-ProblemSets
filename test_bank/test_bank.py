from bank import value


def test_with_hello():
    assert value("hello, madam") == 0
    assert value("heLLo, world!") == 0


def test_with_h():
    assert value("hi!") == 20
    assert value("Hey") == 20


def test_without_h():
    assert value("good morning") == 100
    assert value("wHAt's up?") == 100
