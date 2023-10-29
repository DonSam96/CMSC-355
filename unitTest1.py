import additionCalculator
import unittest

class additionsum(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(additionCalculator.addition(30, 5), 35)
    
if __name__ == '__main__':
    unittest.main()
