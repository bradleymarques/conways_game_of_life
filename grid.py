from coordinates import Coordinates
from cell_state import CellState
import operator
from cell import Cell

class Grid:
    def __init__(self, rows: int = 1, columns: int = 1):
        self.rows = rows
        self.columns = columns
        self._initialize_cells()

    rows = property(operator.attrgetter("_rows"))
    columns = property(operator.attrgetter("_columns"))
    cells = property(operator.attrgetter("_cells"))

    @rows.setter
    def rows(self, new_rows: int):
        if not isinstance(new_rows, int):
            raise TypeError
        if new_rows <= 0:
            raise IndexError
        self._rows = new_rows

    @columns.setter
    def columns(self, new_columns: int):
        if not isinstance(new_columns, int):
            raise TypeError
        if new_columns <= 0:
            raise IndexError
        self._columns = new_columns

    def _initialize_cells(self):
        grid = []

        for r in range(self.rows):
            column = []
            for c in range(self.columns):
                column.append(Cell(CellState.DEAD, Coordinates(r, c)))
            grid.append(column)

        self._cells = grid
