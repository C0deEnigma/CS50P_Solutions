from fuel import convert, gauge
import pytest
def test_convert():
    assert convert('3/4') == 75
    with pytest.raises(ZeroDivisionError):
            assert convert("3/0")
    with pytest.raises(ValueError):
            assert convert("4/3")
    with pytest.raises(ValueError):
            assert convert("cat/dog")
def test_gauge():
    assert gauge(75) == '75%'
    assert gauge(99.2) == 'F'
    assert gauge(99) == 'F'
    assert gauge(0.5) == 'E'
    assert gauge(1) == 'E'
