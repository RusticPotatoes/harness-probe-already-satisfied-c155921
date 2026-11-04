import unittest

from catalog.metrics import work_out_account_figure


class Behaviour(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(work_out_account_figure(*([18, None, 6],)), 12.0)

    def test_case_2(self):
        self.assertEqual(work_out_account_figure(*([18, 6],)), 12.0)

    def test_case_3(self):
        self.assertEqual(work_out_account_figure(*([],)), 0.0)

    def test_case_4(self):
        self.assertEqual(work_out_account_figure(*([None],)), 0.0)

    def test_case_5(self):
        self.assertEqual(work_out_account_figure(*([4],)), 4.0)


if __name__ == "__main__":
    unittest.main()
