import fuel

def test_f_output():
    assert gauge(99) == "F"

def test_e_output():
    assert gauge(1) == "E"

def test_percentage_output():
    assert gauge(14) == "14%"

def test_convert():
    assert convert("3/4") == 75

def test_zero_convert():
    assert conver