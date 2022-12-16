from twttr import shorten

def test_word_with_lower_vowels():
    assert shorten("education") == "dctn"

def test_word_with_upper_vowels():
    assert shorten("EDUCATION") == "DCTN"


def test_word_without_vowels():
    assert shorten("Gym") == "Gym"
def test_numbers():
    with pytest.raises("ValueError")
