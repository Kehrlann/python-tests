from snake import Direction, Snake as CorrectSnake


class Snake(CorrectSnake):
    def change_direction(self, new_direction: Direction) -> bool:
        if new_direction == self.__direction:
            return False
        return super().change_direction(new_direction)
