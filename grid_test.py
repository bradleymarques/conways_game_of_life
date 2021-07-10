from cell_state import CellState
import unittest
from grid import Grid
from cell import Cell
from coordinates import Coordinates

class GridTest(unittest.TestCase):

    def test_default_initialization(self):
        grid = Grid()
        self.assertEqual(1, grid.rows)
        self.assertEqual(1, grid.columns)

    def test_valid_initialization(self):
        grid_1 = Grid(10, 100)
        self.assertEqual(10, grid_1.rows)
        self.assertEqual(100, grid_1.columns)

        grid_2 = Grid(1, 1)
        self.assertEqual(1, grid_2.rows)
        self.assertEqual(1, grid_2.columns)

    def test_invalid_initialization(self):
        self.assertRaises(IndexError, Grid, -10, 10)
        self.assertRaises(IndexError, Grid, -10, 10)
        self.assertRaises(IndexError, Grid, -10, -10)
        self.assertRaises(IndexError, Grid, 1, 0)
        self.assertRaises(IndexError, Grid, 0, 1)
        self.assertRaises(IndexError, Grid, 0, 0)
        self.assertRaises(TypeError, Grid, 1.5, 15)
        self.assertRaises(TypeError, Grid, 15, 1.5)

    def test_initialize_tiny_grid(self):
        grid = Grid(1, 1)
        expected_cells = [
            [
                Cell(CellState.DEAD, Coordinates(0, 0))
            ]
        ]
        actual_cells = grid.cells
        self.assertEqual(1, len(actual_cells))
        self.assertEqual(1, len(actual_cells[0]))

        self.assert_cells_equal(expected_cells[0][0], actual_cells[0][0])

    def test_initialize_small_grid(self):
        grid = Grid(2, 2)
        expected_cells = [
            [
                Cell(CellState.DEAD, Coordinates(0, 0)),
                Cell(CellState.DEAD, Coordinates(0, 1))
            ],
            [
                Cell(CellState.DEAD, Coordinates(1, 0)),
                Cell(CellState.DEAD, Coordinates(1, 1))
            ]
        ]
        actual_cells = grid.cells
        self.assertEqual(2, len(actual_cells))
        self.assertEqual(2, len(actual_cells[0]))

        self.assert_cells_equal(expected_cells[0][0], actual_cells[0][0])
        self.assert_cells_equal(expected_cells[0][1], actual_cells[0][1])
        self.assert_cells_equal(expected_cells[1][0], actual_cells[1][0])
        self.assert_cells_equal(expected_cells[1][1], actual_cells[1][1])


    def assert_cells_equal(self, cell_1: Cell, cell_2: Cell):
        self.assertEqual(cell_1.coordinates, cell_2.coordinates)
        self.assertEqual(cell_1.state, cell_2.state)

if __name__ == "__main__":
    unittest.main()
