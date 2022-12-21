from um import count
import pytest

def test_um():
    assert count("hello, um") == 1
    assert count("copium") == 0
    assert count("um, hello, ok, um") == 2
    assert count("hello,um,ok,um") == 2
    assert count("copium") == 0
    assert count("ferg") == 0
