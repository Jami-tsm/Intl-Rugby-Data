import unittest
from src.parsing import parse_file


class TestParsing(unittest.TestCase):
    def test_csv_rows(self):
        result = parse_file()
        self.assertEqual(len(result), 2784, f"Expected number of rows: 2784 Result: {len(result)} ")  # add assertion here


if __name__ == '__main__':
    unittest.main()
