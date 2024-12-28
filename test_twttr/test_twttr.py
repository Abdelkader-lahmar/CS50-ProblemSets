from twttr import shorten


def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("my name") == "my nm"
    assert shorten("you are my love") == "y r my lv"


def test_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("MY NAME") == "MY NM"
    assert shorten("YOU ARE MY LOVE") == "Y R MY LV"


def test_mixe():
    assert shorten("TwitTER") == "TwtTR"
    assert shorten("My Name") == "My Nm"
    assert shorten("You Are My Love") == "Y r My Lv"


def test_numbers():
    for n in ["15", "34", "0", "-3", "-1"]:
        assert shorten(n) == n


def test_punctuation():
    for pun in [":", ",", ".", ";,./!"]:
        assert shorten(pun) == pun
