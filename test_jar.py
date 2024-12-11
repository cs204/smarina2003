from jar import Jar
import pytest

def test_init():
    jar = Jar (13)
    assert jar.capacity == 13
    with pytest.raises(ValueError):
        Jar(-3)
    with pytest.raises(ValueError):
        Jar(3.5)

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(3)
    with pytest.raises(ValueError):
        jar = Jar(3)
        jar.deposit(-3)

def test_str():
    jar = Jar()
    jar._size = 3
    assert jar.__str__() == 3 * "\N{Cookie}"

def test_withdraw():
    jar = Jar(4)
    jar._size = 3
    jar.withdraw(2)
    assert jar._size == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)
    with pytest.raises(ValueError):
        jar.withdraw(2.5)

def test_capacity():
    jar = Jar()
    jar._capacity = 12
    assert jar.capacity == 12
    jar.capacity = 13
    assert jar.capacity == 13
    with pytest.raises(ValueError):
        jar.capacity = -3
    with pytest.raises(ValueError):
        jar.capacity = 3.5


def test_size():
    jar = Jar()
    jar._capacity = 5
    jar._size = 4
    assert jar.size == 4
    jar.size = 5
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.size = 6
    with pytest.raises(ValueError):
        jar.size = -6
    with pytest.raises(ValueError):
        jar.size = 3.5
