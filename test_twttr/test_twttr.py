from twttr import shorten

def test_word_with_vowels():
    assert shorten("David") == "Dvd"


def test_word_without_vowels():
    assert shorten("Gym") == "Gym"


def