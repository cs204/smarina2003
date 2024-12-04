from bank import value

def test_здравствуйте():
    assert value("Здравствуйте, Гарри!") == "$0"

def test_здрасти():
    assert value("Здрасти, Боб!") == "$20"

def test_hello():
    assert value("Hello, Ron!") == "$100"
