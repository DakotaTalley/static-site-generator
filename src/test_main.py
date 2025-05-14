import unittest

from main import extract_title


class TestHelpers(unittest.TestCase):
    def test_extract_title(self):
        md = "# This is a header"
        self.assertEqual(extract_title(md), "This is a header")

    def test_extract_title_missing(self):
        md = "This is a header"
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()