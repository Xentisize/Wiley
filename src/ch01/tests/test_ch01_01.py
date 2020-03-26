class TestChapter01:
    def test_is_multiple(self):
        from src.ch01.ex_01_01 import is_multiple

        assert is_multiple(100, 10) == True
        assert is_multiple(20, 100) == False
