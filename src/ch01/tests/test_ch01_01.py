class TestChapter01:
    def test_is_multiple(self):
        from src.ch01.ex_01_01 import is_multiple

        assert is_multiple(100, 10) == True
        assert is_multiple(20, 100) == False

    def test_is_even(self):
        from src.ch01.ex_01_02 import is_even

        assert is_even(100) == True
        assert is_even(301) == False
        assert is_even(-110) == True
        assert is_even(-101) == False

    def test_minmax(self):
        from src.ch01.ex_01_03 import minmax
        import random

        data = [15, 60, 80, 120, 30, 10]
        assert minmax(data) == (10, 120)

        data = [-15, 60, 80, 121, 31, 11]
        assert minmax(data) == (-15, 121)

    def test_sqrt_list(self):
        from src.ch01.ex_01_04 import sqrt_list

        assert sqrt_list(5) == [1, 4, 9, 16]
        assert sqrt_list(10) == [1, 4, 9, 16, 25, 36, 49, 64, 81]
