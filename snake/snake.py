from enum import Enum
from http.client import FORBIDDEN


position = tuple[int, int]


class Direction(Enum):
    UP: position = (0, -1)
    DOWN: position = (0, 1)
    LEFT: position = (-1, 0)
    RIGHT: position = (1, 0)


class Snake:
    """
    The Snake.

        Attributes:
            segments : list[position]
                the "pieces" of the snake
    """
    segments: list[position]
    __direction: Direction # not documented, this is private!

    def __init__(self, segments: list[position], initial_direction: Direction) -> None:
        """
        """
        self.segments = segments
        self.__direction = initial_direction

    def change_direction(self, new_direction: Direction) -> bool:
        """
        Changes the current direction, if allowed. The snake cannot "turn back".

            Parameters:
                new_direction : Direction

            Returns:
                succeeded (bool) : True if the change was allowed, False otherwise.
        """
        forbidden_direction_changes = (
            (Direction.UP, Direction.DOWN),
            (Direction.DOWN, Direction.UP),
            (Direction.LEFT, Direction.RIGHT),
            (Direction.RIGHT, Direction.LEFT)
        )

        if (self.__direction, new_direction) in forbidden_direction_changes:
            return False
        else:
            self.__direction = new_direction
            return True

    def move(self) -> None:
        """Make the snake move in the current direction. After calling it, the "segments" list is updated."""
        head_x, head_y = self.segments[-1]
        dir_x, dir_y = self.__direction.value
        new_head = (head_x + dir_x, head_y + dir_y)
        self.segments.pop(0)
        self.segments.append(new_head)
