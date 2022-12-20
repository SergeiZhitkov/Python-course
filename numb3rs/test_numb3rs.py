from numb3rs import validate

def test_valid_data():
    assert validate("255.255.255.255") == True
    assert validate("99.99.99.99") == True
    assert validate("255.94.5.0") == True

def test_invalid_data():
    assert validate("256.0.43.3") == False
    assert validate("frg")  == False
    assert validate("34.45") == False