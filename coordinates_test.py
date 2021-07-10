import unittest
from coordinates import Coordinates

class CoordinatesTest(unittest.TestCase):

    def test_default_initialization(self):
        coordinates = Coordinates()
        self.assertEqual(0, coordinates.x)
        self.assertEqual(0, coordinates.y)

    def test_non_default_initializations(self):
        coordinates_1 = Coordinates(x = 1)
        self.assertEqual(1, coordinates_1.x)
        self.assertEqual(0, coordinates_1.y)

        coordinates_2 = Coordinates(y = 1)
        self.assertEqual(0, coordinates_2.x)
        self.assertEqual(1, coordinates_2.y)

        coordinates_3 = Coordinates(x = 1, y = 1)
        self.assertEqual(1, coordinates_3.x)
        self.assertEqual(1, coordinates_3.y)

    def test_valid_initializations(self):
        Coordinates(16,0)
        Coordinates(-100,0)
        Coordinates(0,1000)
        Coordinates(0,-11000)
        Coordinates(15,15)
        Coordinates(0,0)
        Coordinates(-15,-15)

    def test_invalid_initializations(self):
        self.assertRaises(TypeError, Coordinates, [1.1, 1])
        self.assertRaises(TypeError, Coordinates, [1, 1.1])
        self.assertRaises(TypeError, Coordinates, [True, 0])
        self.assertRaises(TypeError, Coordinates, [0, False])
        self.assertRaises(TypeError, Coordinates, [None, 0])
        self.assertRaises(TypeError, Coordinates, [0, None])
        self.assertRaises(TypeError, Coordinates, [None, None])
        self.assertRaises(TypeError, Coordinates, ["15", 0])
        self.assertRaises(TypeError, Coordinates, [0, "15"])

if __name__ == '__main__':
    unittest.main()
