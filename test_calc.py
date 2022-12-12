from unittest import TestCase
from calc import div


class TestCalc(TestCase):
    def test_div(self):
        self.assertEqual(5, div(10, 2))
        self.assertEqual(5, div(12, 2))
        with self.assertRaises(ValueError):
            div(8, 0)
