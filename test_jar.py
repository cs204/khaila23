from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar(-3)
    with pytest.raises(ValueError):
        Jar(3.5)

def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.deposit(100)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(3)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(6)

def teststr():
    jar = Jar()
    jar.deposit(3)
    assert jar.__str__() == 3 * "\N{Cookie}"
    jar.deposit(1)


test_init()
test_deposit()
test_withdraw()
teststr()
