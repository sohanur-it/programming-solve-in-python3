from fibo import add, is_even

def test_add():
    assert add(2, 3) == 5

def test_is_even():
    assert is_even(2) == True