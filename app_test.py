"""Unit test file for app.py"""
from app import returnBackwardsString
import unittest

class TestApp(unittest.TestCase):
    """Unit tests defined for app.py"""

    def test_return_backwards_string(self):
        """Test return backwards simple string"""
        self.assertEqual(returnBackwardsString('hello'), 'olleh')

if __name__ == '__main__':
    unittest.main()