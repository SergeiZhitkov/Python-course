from working import convert
import pytest

def test_with_minutes:
    assert convert("12:00 AM to 2:00 PM") == "00:00 to 14:00"
    assert convert("10:34 AM to 6:59 PM") == "10:34 to 18:59"
    assert convert("12:00 PM to 2:00 AM") == "12:00 to 02:00"
    assert convert("10:34 PM to 6:59 AM") == "22:34 to 06:59"

def test_without_minutes:
    assert convert("12 AM to 2 PM") == "00:00 to 14:00"
    assert convert("10 AM to 6 PM") == "10:00 to 18:00"
    assert convert("12 PM to 2 AM") == "12:00 to 02:00"
    assert convert("10 PM to 6 AM") == "22:00 to 06:00"

def test_value_error():
    with pytest.raises(ValueError)
    


