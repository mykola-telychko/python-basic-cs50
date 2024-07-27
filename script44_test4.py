# python -m pytest - command for check pytest
from script44 import square 

def test_square(): 
    assert square(2) == 4
    assert square(3) == 9

def test_square(): 
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero(): 
    assert square(0) == 0