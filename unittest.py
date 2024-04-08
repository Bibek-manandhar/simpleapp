import unittest
from my_application import my_function

class TestMyFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(my_function(2), 4)  # Passes
    
    def test_case_2(self):
        self.assertEqual(my_function(3), 9)  # Passes
    
    def test_case_3(self):
        self.assertEqual(my_function(0), 0)  # Passes
    
    def test_case_4(self):
        self.assertEqual(my_function(5), 25)  # Fails
    
    def test_case_5(self):
        self.assertEqual(my_function(-1), 1)  # Fails

if __name__ == '__main__':
    unittest.main()
