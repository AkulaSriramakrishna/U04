import unittest

def addition(a,b):
    return a+b

class MyTestCase(unittest.TestCase):
    def test_postive_number(self):
        result=addition(1,2)
        self.assertEquals(result,3,'Not correct')

    def test_negative_number(self):
        result = addition(1 , -2)
        self.assertEquals(result, -1, 'Not correct')
    def test_zero_number(self):
        result = addition(0 , -2)
        self.assertEquals(result, -2, 'Not correct')