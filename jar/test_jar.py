from jar import Jar
import pytest
def test_init():
    jar=Jar()
def test_deposit():
    jar=Jar()
    with pytest.raises(ValueError):
        assert Jar.deposit(jar,-1)
    with pytest.raises(ValueError):
        assert Jar.deposit(jar,1.4)
    with pytest.raises(ValueError):
        assert Jar.deposit(jar,14)
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"
def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(1)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(15)

