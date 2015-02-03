__author__ = 'stefanos'


class GameOfLife:
    """
    Game of Life class
    """

    def __init__(self, seed):
        pass

    def next(self):
        return set()


def test_blinker_pattern():
    """
    .....
    .***.
    .....

    =>

    ..*..
    ..*..
    ..*..
    """

    seed = {(1, 1), (2, 1), (3, 1)}
    game = GameOfLife(seed)
    assert game.next() == {(2, 0), (2, 1), (2, 2)}
    assert game.next() == seed


def test_beacon_pattern():
    """
    **..
    **..
    ..**
    ..**

    =>

    **..
    *...
    ...*
    ..**

    =>

    **..
    **..
    ..**
    ..**

    """

    seed = {(0, 0), (1, 0), (0, 1), (1, 1), (2, 2), (3, 2), (2, 3), (3, 3)}
    game = GameOfLife(seed)
    assert game.next() == {(0, 0), (1, 0), (0, 1), (3, 2), (2, 3), (3, 3)}
    assert game.next() == seed