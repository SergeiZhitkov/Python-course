import pytest
from seasons import how_many_minutes
def test_valid_date():
    assert how_many_minutes("2001-09-03") == "sixteen billion, one hundred forty million, nine hundred two thousand, four hundred"
    assert how_many_minutes("2022-12-26") == "zero"

def test_invalid_date():
    with pytest.raises(SystemExit):
        how_many_minutes("2023.09.03")
    with pytest.raises(SystemExit):
        how_many_minutes("bgnthm")
    with pytest.raises(SystemExit):
        how_many_minutes("2022-12-54")
    with pytest.raises(SystemExit):
        how_many_minutes("2022-43-05")
    with pytest.raises(SystemExit):
        how_many_minutes("100000-02-03")
