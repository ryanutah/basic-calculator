import math
import pytest
from Functions import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add("2", "3") == 5
    assert math.isclose(add(2.5, 0.5), 3.0)

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract("5", "2") == 3

def test_multiply():
    assert multiply(4, 3) == 12
    assert math.isclose(multiply(2.5, 2), 5.0)

def test_divide_normal():
    assert divide(10, 2) == 5
    assert math.isclose(divide(7, 2), 3.5)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

@pytest.mark.parametrize("bad", ["a", object(), None])
def test_type_errors(bad):
    import Functions
    with pytest.raises(TypeError):
        Functions.add(bad, 1)
    with pytest.raises(TypeError):
        Functions.subtract(1, bad)
    with pytest.raises(TypeError):
        Functions.multiply(bad, bad)
    with pytest.raises(TypeError):
        Functions.divide(bad, 1)
