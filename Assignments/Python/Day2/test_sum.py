import pytest


def test_sum():
    assert 1==1

def test_minus():
    assert 0==0

@pytest.mark.skip
def test_mul():
    assert 2*2 == 4