import main

class TestMain1:
    def test_Fibo_cor_n(self):
        assert main.Fibona(5) == [1, 1, 2, 3, 5]

    def test_Fibonacchi_cor_n_and_incor_result(self):
        assert main.Fibona(3) == [0, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_Fibonacchi_on_incor_n(self):
        assert main.Fibona("10") == [1, 1, 2, 3, 5, 8, 13, 21, 34]