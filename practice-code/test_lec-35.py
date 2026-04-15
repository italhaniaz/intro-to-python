from lec_35 import div

def test_div():
    assert div(4, 2) == 2

def test_div_2():
    assert div(6, 2) == 3

def test_div_for_float():
    assert div(1, 2) == 0.5