from numb3rs import validate

def test_valid_data():
    assert validate("255.255.255.255") == True
    assert validate("99.99.99.99") == True
    assert validate("0.0.0.0") == True
    assert validate("255.94.5.0") == True

def test_invalid_data():
    assert validate("256.0.43.3") == False
    assert validate("04.0.2.4")  == False
    assert validate("012.3.24.2")  == False
    assert validate("frg.0.3.4")  == False
    assert validate("....")  == False