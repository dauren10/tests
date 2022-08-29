import pytest

@pytest.mark.one
def test_method1():
    x=10
    y=5
    assert x == y

@pytest.mark.two
def test_method2():
    a=15
    b=20

    assert a + 5 == b