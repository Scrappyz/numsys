import sys, pathlib, unittest

sys.path.append(str(pathlib.Path(__file__).parents[1].joinpath("project").resolve()))

import main

class TestNumSys(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(main.convert("3b4.C8", 16, 10, False), "948.78125")

if __name__ == "__main__":
    unittest.main()