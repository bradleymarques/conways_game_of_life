from cell_state import CellState
import unittest
from cell import Cell

class CellTest(unittest.TestCase):

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
        cell.setState(CellState.ALIVE)
        self.assertEqual(CellState.ALIVE, cell.state)

    def test_set_state_from_alive_to_dead(self):
        cell = Cell(CellState.ALIVE)
        self.assertEqual(CellState.ALIVE, cell.state)
        cell.setState(CellState.DEAD)
        self.assertEqual(CellState.DEAD, cell.state)

if __name__ == '__main__':
    unittest.main()
