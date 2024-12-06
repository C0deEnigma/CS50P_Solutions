from bank import value
def test_value():
    assert value('Hello, sk') == 0
    assert value('hello, sk') == 0
    assert value('HELLO, sk') == 0
    assert value('hii, bro') == 20
    assert value('Hii, bro') == 20
    assert value('greetings bro') == 100
