import unittest
from Calculadora import fatorial

class TestCalculadora(unittest.TestCase):

    def test_fatorial_de_5(self):
        self.assertEqual(fatorial(5), 120)

    def test_fatorial_de_1(self):
        self.assertEqual(fatorial(1), 1)

    def test_fatorial_de_0(self):
        self.assertEqual(fatorial(0), 1)

if __name__ == "__main__":
    unittest.main()