from snake import Snake, Direction
# from broken_snake import Snake, Direction


def test_move_right() -> None:
    # Snake looks like this:
    #
    #    column 5 6 7 8
    # line
    #  4        x x
    #  5          x >
    #
    # After a move, it should look like:
    #
    #    column 5 6 7 8
    # line
    #  4          x
    #  5          x x >
    snake: Snake = Snake(
        [(5, 4), (6, 4), (6, 5), (7, 5)],
        Direction.RIGHT
    )
    snake.move()
    assert snake.segments == [(6, 4), (6, 5), (7, 5), (8, 5)]


# TODO: test "change direction"