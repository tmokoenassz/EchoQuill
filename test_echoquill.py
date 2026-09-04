# test_echoquill.py
"""
Tests for EchoQuill module.
"""

import unittest
from echoquill import EchoQuill

class TestEchoQuill(unittest.TestCase):
    """Test cases for EchoQuill class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EchoQuill()
        self.assertIsInstance(instance, EchoQuill)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EchoQuill()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
