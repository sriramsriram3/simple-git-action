from src.math import sub,add

def test_addexample():
    assert add(2,3) == 5
    assert add(4,6) == 10
    assert add(0,0) == 0
    assert add(-1,-1) == -2

def test_subexample():
    assert sub(3,2) == 1
    assert sub(-1,-1) == 0
    assert sub(2,-5) ==-3
    assert sub(0,0) == 0