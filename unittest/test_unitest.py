import unittest
from full_name import full_name

class NameTestCase(unittest.TestCase):
    """test"""

    def test_first_last_name(self):
        format_name = full_name('shalabayev','dauren')
        self.assertEqual(format_name,'Shalabayev Dauren')

    def test_first_last_middle(self):
        format_name = full_name('shalabayev','dauren','amangeldyevich')
        self.assertEqual(format_name,'Shalabayev Dauren Amangeldyevich')

if __name__ == "__main__":
    unittest.main()