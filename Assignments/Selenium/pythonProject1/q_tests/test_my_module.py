import unittest

def mutliplt(a,b):
    return a*b

def addition(a,b):
    return a+b

class MyTestCase(unittest.TestCase):

    def setUp(self):
        print('This is setup enviroment')

    def tearDown(self):
        print('Cleaning enviroment bt deleting the data created during test')

    def test_function(self):
        #code
        self.assertEquals(1,1)
        pass

    def test_positive_number(self):
        result=mutliplt(1,2)
        self.assertEquals(result,2)

    def test_negative_number(self):
        result=mutliplt(-1,-2)
        self.assertEquals(result,2)

    def test_zero_number(self):
        result = mutliplt(0,-2)
        self.assertEquals(result, 0)
    def test_upper(self):
        self.assertTrue('FOO'.isupper())

    def test_lowerr(self):
        self.assertTrue('FOO'.islower())

    def test_bad_multiplication(self):
        with self.assertRaises(TypeError):
            result = mutliplt('apple', 'r')
            self.assertRaises(result,3)

    @unittest.skip('Reason is nothing')
    def test_skip(self):
        pass