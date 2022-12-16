from bank import value
def main():
    test_with_hello()
    test_with_h()
    test_without_first_h()
    test_with_numbers()
    test_with_punctuations()


def test_with_hello():
    assert value("Hello, Jhon") == "$0"
    assert value("hello, Jhon") == "$0"

def test_with_h():
    assert value("Hi, Mark") == "$20"
    assert value("hi, Mark") == "$20"

def test_without_first_h():
    assert value("Good morning, Jhon") == "$100"
    assert value("nice to meet you!") == "$100"

def test_with_numbers():
    assert value("01234Hello") == "$100"

def test_with_punctuations():
    assert value("__Hello, Jhon") == "$100"

if __name__ == "__main__":
    main()