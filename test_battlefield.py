from battlefield import Battlefield
import unittest

class TestBuildFleet(unittest.TestCase):
    """Test build fleet method in battlefield"""
    def setUp(self):
        self.battlefield = Battlefield()

    def test_build_fleet(self):
        """Test to ensure fleet is built off user input"""
        fleet_side = len(self.battlefield.build_fleet())
        self.assertEqual(fleet_side,3)


if __name__ == "__main__":
    unittest.main()

