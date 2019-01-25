import unittest
import sys
sys.path.append('../')
from calculator import Calculator

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.calc = Calculator()
    print('Set up class')
    # Create an instance of the calculator that can be used in all tests

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_add(self):
    result = self.calc.add(2, 7)
    expected = 9
    self.assertEqual(result, expected)
    # self.assertEqual(self.calc.add(2, 7), 9)

  def test_subtract(self):
    result = self.calc.subtract(7, 2)
    expected = 5
    self.assertEqual(result, expected)

  def test_multiply(self):
    result = self.calc.multiply(2, 7)
    expected = 14
    self.assertEqual(result, expected)

  def test_divide(self):
    result = self.calc.divide(10, 2)
    expected = 5
    self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()