import pytest
from seasons import how_many_minutes
def test_valid_date():
    assert how_many_minutes("2001-09-03") == "sixteen billion, one hundred forty million, nine hundred two thousand, four hundred"
    assert how_many_minutes("2022-12-26") == "zero"

def test_invalid_date():
    assert how_many_times("2023.09.03") == "Invalid date"
    assert how_many_times("bgnthm") == "Invalid date"
    assert how_many_times("2022-12-54") == "Invalid date"