import sys, pathlib, unittest

sys.path.append(str(pathlib.Path(__file__).parents[1].joinpath("project").resolve()))

import main

class TestNumSys(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(main.convert("29", 10, 2), "11101")
        self.assertEqual(main.convert("11101", 2, 10), "29")
        self.assertEqual(main.convert("25", 8, 10), "21")
        self.assertEqual(main.convert("25", 8, 2), "10101")
        self.assertEqual(main.convert("10101", 2, 16), "15")
        self.assertEqual(main.convert("3b4.C8", 16, 10), "948.78125")
        
        self.assertRaises(Exception, main.convert, "3", 2, 12)
        self.assertRaises(Exception, main.convert, "3", 12, 2)

if __name__ == "__main__":
    unittest.main()