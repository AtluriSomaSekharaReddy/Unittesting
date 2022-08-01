
from divide import divide
 
import unittest
class TestingDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(4,1),4,"It should be 5")
    def test_divide2(self):
        self.assertEqual(divide(22,-2),-11)
    def test_divide3(self):
        self.assertAlmostEqual(divide(88,7),12.571428571)
    def test_divide4(self):
        self.assertRaises(ValueError,divide,10,0)
        self.assertRaises(ValueError,divide,"hi","hlo")
        self.assertRaises(ValueError,divide,[12],[1,3])
if __name__ == '__main__':  
    unittest.main()  


