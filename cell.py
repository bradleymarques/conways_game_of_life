import operator
from cell_state import CellState

##
# Models a single Cell in a Grid in the Game of Life
# A Cell can either be alive or dead
#
class Cell:
    def __init__(self, state: CellState = CellState.DEAD):
        self.state = state

    state = property(operator.attrgetter("_state"))

    @state.setter
    def state(self, new_state: CellState):
        if new_state in CellState:
            self._state = new_state
        else:
            raise TypeError
