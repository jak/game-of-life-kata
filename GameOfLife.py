__author__ = 'stefanos'


class GameOfLife:
    """
    Game of Life class
    """

    state = set()

    def __init__(self, seed):
      self.state = seed

    def next(self):
        new_state = set()
        for cell in self.state:
          if self.should_stay_alive(cell):
            new_state.add(cell)

        self.state = new_state
        return new_state

    def c2p(self, cell):
      return cell.point()

    def should_stay_alive(self, cell):
      alive_neighbours = self.neighbours(cell) & self.state
      print alive_neighbours
      return len(alive_neighbours) in [2,3]

    def is_alive(self, cell):
      return cell in self.state

    def neighbours(self, cell):
      cells = set()
      for x in range(-1,2):
        for y in range(-1,2):
          if x != 0 or y != 0:
            cells.add((cell[0] + x, cell[1] + y))
      return cells

def test_single_cell_dies():
  seed = set([(0, 0)])
  game = GameOfLife(seed)
  assert game.next() == set()

def test_one_neighbour_dies():
  seed = set([(0,0), (1,0)])
  game = GameOfLife(seed)
  assert game.next() == set()

def test_block_pattern():
  """
  **-
  **-
  ---
  """
  seed = set([(0,0), (1,0), (0, 1), (1,1)])
  game = GameOfLife(seed)
  assert game.next() == seed

def hid_test_blinker_pattern():
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


def hid_test_beacon_pattern():
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
