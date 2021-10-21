from battlefield import Battlefield
from fleet import Fleet
from battlefield import fleet1
import unittest

fleet1 = []

class TestBuildFleet(unittest.TestCase):
    """Test build fleet method in battlefield"""
    def setUp(self):
        self.battlefield = Battlefield()

    def test_build_fleet(self):
        """Test to ensure fleet is built off user input"""
        fleet_test = Fleet()
        fleet1.append(fleet_test.build_fleet())
        fleet_size = len(fleet1)
        self.assertEqual(fleet_size,1)


if __name__ == "__main__":
    unittest.main()

