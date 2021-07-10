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

    def test_set_x_and_y(self):
        coordinates = Coordinates()
        self.assertEqual(0, coordinates.x)
        self.assertEqual(0, coordinates.y)

        coordinates.x = 5
        self.assertEqual(5, coordinates.x)
        self.assertEqual(0, coordinates.y)

        coordinates.y = -100
        self.assertEqual(5, coordinates.x)
        self.assertEqual(-100, coordinates.y)

    def test_set_invalid_x_and_y(self):
        coordinates = Coordinates()
        self.assertRaises(TypeError, coordinates.x, "Mountaineer")
        self.assertRaises(TypeError, coordinates.y, "Mountaineer")
        self.assertRaises(TypeError, coordinates.x, 1.0001)
        self.assertRaises(TypeError, coordinates.y, 1.0001)
        self.assertRaises(TypeError, coordinates.x, True)
        self.assertRaises(TypeError, coordinates.y, True)
        self.assertRaises(TypeError, coordinates.x, None)
        self.assertRaises(TypeError, coordinates.y, None)

    def test_coordinate_equality(self):
        coordinates_1 = Coordinates(0, 1)
        coordinates_2 = Coordinates(0, 1)
        coordinates_3 = Coordinates(-10, 156)
        coordinates_4 = Coordinates(-10, 156)

        self.assertTrue(coordinates_1 == coordinates_2)
        self.assertTrue(coordinates_2 == coordinates_1)
        self.assertTrue(coordinates_3 == coordinates_4)
        self.assertTrue(coordinates_4 == coordinates_3)

        self.assertFalse(coordinates_1 == coordinates_3)
        self.assertFalse(coordinates_4 == coordinates_1)
        self.assertFalse(coordinates_2 == coordinates_3)
        self.assertFalse(coordinates_4 == coordinates_2)

if __name__ == '__main__':
    unittest.main()
