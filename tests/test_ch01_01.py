from src.ch01 import ex_01_01


def test_is_multiple():
    assert ex_01_01.is_multiple(100, 10) == True
    assert ex_01_01.is_multiple(20, 100) == False
