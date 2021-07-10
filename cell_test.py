import unittest
from cell_state import CellState
from cell import Cell
from coordinates import Coordinates

class CellTest(unittest.TestCase):

    def test_default_initialization(self):
        cell = Cell()
        self.assertEqual(CellState.DEAD, cell.state)

    def test_initialization_of_dead_cell(self):
        cell = Cell(CellState.DEAD)
        self.assertEqual(CellState.DEAD, cell.state)

    def test_initialization_of_alive_cell(self):
        cell = Cell(CellState.ALIVE)
        self.assertEqual(CellState.ALIVE, cell.state)

    def test_invalid_initialization(self):
        self.assertRaises(TypeError, Cell, 0)
        self.assertRaises(TypeError, Cell, None)
        self.assertRaises(TypeError, Cell, True)
        self.assertRaises(TypeError, Cell, "Alive")
        self.assertRaises(TypeError, Cell, "Hello")

    def test_set_state_from_dead_to_alive(self):
        cell = Cell(CellState.DEAD)
        self.assertEqual(CellState.DEAD, cell.state)
        cell.state = CellState.ALIVE
        self.assertEqual(CellState.ALIVE, cell.state)

    def test_set_state_from_alive_to_dead(self):
        cell = Cell(CellState.ALIVE)
        self.assertEqual(CellState.ALIVE, cell.state)
        cell.state = CellState.DEAD
        self.assertEqual(CellState.DEAD, cell.state)

    def test_set_invalid_state(self):
        cell = Cell(CellState.ALIVE)
        self.assertRaises(TypeError, cell.state, "Dead parrot")
        self.assertRaises(TypeError, cell.state, 0)
        self.assertRaises(TypeError, cell.state, False)
        self.assertRaises(TypeError, cell.state, None)

if __name__ == '__main__':
    unittest.main()
