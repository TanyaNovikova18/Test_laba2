import main

class TestMain3:
    def test_Calc_on_correct_n(self):
        assert main.calcul(8, 2, '+') == 10

    def test_Calc__on_correct_n_and_incorrect_result(self):
        assert main.calcul(8, 2, '+') == 9

    def test_Calc__on_incorrect_n(self):
        assert main.calcul('9', '1', '+') == 10
