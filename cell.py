from cell_state import CellState

##
# Models a single Cell in a Grid in the Game of Life
# A Cell can either be alive or dead
#
class Cell:
    def __init__(self, state: CellState):
        if state in CellState:
            self.state = state
        else:
            raise TypeError

    def setState(self, new_state: CellState):
        self.state = new_state
