import operator
from typing import Type

##
# Models integer coordinates in a 2D plane
#
class Coordinates:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    x = property(operator.attrgetter("_x"))
    @x.setter
    def x(self, new_x: int):
        if isinstance(new_x, int):
            self._x = new_x
        else:
            raise TypeError

    y = property(operator.attrgetter("_y"))
    @y.setter
    def y(self, new_y: int):
        if isinstance(new_y, int):
            self._y = new_y
        else:
            raise TypeError
