# test_calculator.py - Basic tests with obvious gaps

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        # ISSUE: Only tests happy path
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
        
    # ISSUE: Missing test for divide method (especially division by zero!)
    # ISSUE: No tests for calc_stuff or apply_tax methods
    # ISSUE: No edge case testing

if __name__ == "__main__":
    unittest.main()