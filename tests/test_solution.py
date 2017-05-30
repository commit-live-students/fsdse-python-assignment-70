from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        x = [0, 10, 20, 40, 60]
        y = [10, 30, 40]

        res = solution(x, y)

        self.assertNotEqual(None, res)
        self.assertEqual(res[0], 10)
        self.assertEqual(res[1], 40)
