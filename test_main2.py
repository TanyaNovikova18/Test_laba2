import main

class TestMaon:
    def test_Puzirec_on_correct_a(self):
        assert main.puz([5, 8, 1, 3, 9, 12, 0]) == [0, 1, 3, 5, 8, 9, 12]

    def test_Puzirec_on_correct_a_and_incorrect_result(self):
        assert main.puz([5, 8, 1, 3, 9, 12, 0]) == [5, 8, 1, 3, 9, 12, 0]

    def test_Puzirec_on_incorrect_a1(self):
        assert main.puz([5, '8', 1, 3, '9', 12, 0]) == [1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_Puzirec_on_incorrect_a2(self):
        assert main.puz('World$Cool') == [1, 1, 2, 3, 5, 8, 13, 21, 34]