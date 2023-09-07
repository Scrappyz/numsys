import sys, pathlib, unittest

sys.path.append(str(pathlib.Path(__file__).parents[1].joinpath("project").resolve()))

import numsys

class TestNumSys(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(numsys.convert("29", 10, 2), "11101")
        self.assertEqual(numsys.convert("11101", 2, 10), "29")
        self.assertEqual(numsys.convert("25", 8, 10), "21")
        self.assertEqual(numsys.convert("25", 8, 2), "10101")
        self.assertEqual(numsys.convert("10101", 2, 16), "15")
        self.assertEqual(numsys.convert("3b4.C8", 16, 10), "948.78125")
        
        self.assertRaises(Exception, numsys.convert, "3", 2, 12)
        self.assertRaises(Exception, numsys.convert, "3", 12, 2)

if __name__ == "__main__":
    unittest.main()