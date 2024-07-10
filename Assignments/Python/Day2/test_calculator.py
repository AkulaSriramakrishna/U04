import pytest
import Calculator as calc

def test_sum():
    assert calc.sum(5,2) == 7,'Error'

def test_multiplication():
    assert calc.multiplication(5,2) == 10 ,'Multiplication error'

def test_substraction():
    assert calc.substraction(5,3) == 2, 'substraction error'

def test_divison():
    assert  calc.divison(10,2)==5,'Divison error'

@pytest.mark.smoke
def test_one():
    assert 1==1

@pytest.mark.smoke
def test_two():
    assert 1==1