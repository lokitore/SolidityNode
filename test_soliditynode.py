# test_soliditynode.py
"""
Tests for SolidityNode module.
"""

import unittest
from soliditynode import SolidityNode

class TestSolidityNode(unittest.TestCase):
    """Test cases for SolidityNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityNode()
        self.assertIsInstance(instance, SolidityNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SolidityNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
