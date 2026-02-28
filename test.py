import unittest
import exm

class testquiz(unittest.TestCase):

    def test_quiz(self):
        c, t, h, l = exm.dat(0, 0, 0, 100, 80)
        self.assertEqual(c, 1)
        self.assertEqual(t, 80)
        self.assertEqual(h, 80)
        self.assertEqual(l, 80)


def test_average(self):
    c, t, h, l = exm.dat(2, 160, 80, 80, 80)
    
    avg = t / c
    
    self.assertEqual(avg, 80)
    
if __name__ == "__main__":
    unittest.main()
    