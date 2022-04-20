# board
# grid
# tile
# you make a board instance
# you can update board
# you can update a grid
# you can update a tile
from typing import List
import numpy as np


class Grid:
    """
    A Grid is made up of 3x3 tiles, each tile has a single number
    """
    pass


class Board:
    """
    A Board is made up of 3x3 grids
    """
    the_board = None

    def __init__(self, values: List):
        x_counter = 0
        y_counter = 0
        scale = 9
        board = np.empty(shape=(scale, scale))

        counter = 0
        # todo check len(values) == 81, or scale^2
        for x in range(scale):
            for y in range(scale):
                # TODO check value is int, between 1 and 9
                board[x, y] = values[counter]
                counter += 1
        print(board)

        for value in values:
            # print(f"y: {y_counter}, x: {x_counter}")
            board[y_counter, x_counter] = value

            x_counter += 1
            if x_counter > 8:
                x_counter = 0
                y_counter += 1

        print(board)


    def edit_row(self, y_pos: int, values: [int]) -> None:
        pass

    def edit_column(self, x_pos: int, values: [int]) -> None:
        pass

    def edit_single_tile(self, y_pos: int, x_pos: int, value: int) -> None:
        pass

    def verify(self):
        pass
        # for a_grid in self.the_board:
        #     self.verify_square(a_grid)
        #     self.verify_horizontal(a_grid)
        #     self.verify_vertical(a_grid)

    def verify_square(self, a_grid: Grid):
        pass

    def verify_horizontal(self, a_grid: Grid):
        pass

    def verify_vertical(self, a_grid: Grid):
        pass


# i = Board([1, 2, 3, 4, 5, 6, 8, 2, 4, 6, 8, 2, 9, 3, 1, 4, 6, 7, 8])

# load in y 8, x = 0
j = Board(
    [8, 2, 7, 1, 5, 4, 3, 9, 6,
     9, 6, 5, 3, 2, 7, 1, 4, 8,
     3, 4, 1, 6, 8, 9, 7, 5, 2,
     5, 9, 3, 4, 6, 8, 2, 7, 1,
     4, 7, 2, 5, 1, 3, 6, 8, 9,
     6, 1, 8, 9, 7, 2, 4, 3, 5,
     7, 8, 6, 2, 3, 5, 9, 1, 4,
     1, 5, 4, 7, 9, 6, 8, 2, 3,
     2, 3, 9, 8, 4, 1, 5, 6, 7])
