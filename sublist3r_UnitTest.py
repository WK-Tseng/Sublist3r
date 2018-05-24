import unittest
import sublist3r 

class CalculatorTest(unittest.TestCase):                 

    def test_mod_with_remainder(self):                   
        sublist3r.banner()
        #cal = Calculator()
        #self.assertEqual(cal.mod(5, 3), (1, 2))          
'''
    def test_mod_without_remainder(self):
        cal = Calculator()
        self.assertEqual(cal.mod(8, 4), (1, 0))          

    def test_mod_divide_by_zero(self):
        cal = Calculator()
        self.assertRaises(ZeroDivisionError, cal.mod, 7, 1)   
'''

if __name__ == '__main__':
    unittest.main()  