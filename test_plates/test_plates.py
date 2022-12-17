from plates import is_valid

def test_valid_plate():
    assert is_valid("hello2") == True
    assert is_valid("hi") == True

def test_numbers_first():
    assert is_valid("12nice") == False

def test_numbers_in_miidle():
    assert is_valid("ni12ce") == False

def test_zero_first():
    assert is_valid("nice01") == False

def test_invalid_len():
    assert is_valid("toolong") == False
    assert is_valid("z") == False

def test_punctuation():
    assert is_valid("__nice") == False

def test_all_numeric():
    assert is_valid("12345") == False

def test_space():
    assert is_valid("hehe 12") == False