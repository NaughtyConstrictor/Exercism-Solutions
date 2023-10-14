from enum import Enum
import math

class CircleRadius(Enum):
    def __init__(self, radius, score):
        self._value_ = radius
        self.score = score

    INNER_CIRCLE = 1, 10
    MIDDLE_CIRCLE = 5, 5
    OUTER_CIRCLE = 10, 1

    def __ge__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return self.value >= other


def score(x, y):
    """Returns the earned points in a signle toss of a Darts game."""

    dist_from_center = math.hypot(x, y)

    for radius in CircleRadius:
        if dist_from_center <= radius:
            return radius.score
    
    return 0