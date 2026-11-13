
import unittest

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10,20),30)

    def test_subtract(self):
        self.assertEqual(subtract(20,10),10)

    def test_multiply(self):
        self.assertEqual(multiply(10,14),140)

if __name__ == "__main__":
    print("Student calculator application")
    print("Addition:",add(20,20))
    print("Subtraction:",subtract(2,1))
    print("Multiplication:",multiply(5,4))

    unittest.main(argv=['first-arg-is-ignored'], exit=False)
