from coordinates import Coordinates
import operator
from cell_state import CellState

##
# Models a single Cell in a Grid in the Game of Life
# A Cell can either be alive or dead
#
class Cell:
    def __init__(
        self,
        state: CellState = CellState.DEAD,
        coordinates: Coordinates = Coordinates()
        ):
        self.state = state
        self.coordinates = coordinates

    state = property(operator.attrgetter("_state"))
    coordinates = property(operator.attrgetter("_coordinates"))

    @state.setter
    def state(self, new_state: CellState):
        if new_state in CellState:
            self._state = new_state
        else:
            raise TypeError

    @coordinates.setter
    def coordinates(self, new_coordinates: Coordinates):
        if isinstance(new_coordinates, Coordinates):
            self._coordinates = new_coordinates
        else:
            raise TypeError
