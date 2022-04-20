#!/usr/bin/python3
"""

"""
from typing import List
import numpy as np

DEBUG = True
# We are dealing with just 3x3 grids so max is fixed
MAX_SCALE = 9


def check_single_digit_int(single_int: int) -> bool:
    try:
        single_int += 1
        single_int -= 1
    except TypeError:
        raise Exception(f"single_int provided IS NOT INT -> {single_int}")

    if 9 >= single_int >= 1:
        return True
    raise Exception(f"single_int proved IS NOT a single digit int between 1 and 9 -> {single_int}")


def dbg(msg: str) -> None:
    if DEBUG:
        print(msg)


class Board:
    """
    A Board is made up of 9x9 "tiles"
    """
    the_board = None

    def __init__(self, values: List):
        if len(values) != MAX_SCALE*MAX_SCALE:
            raise Exception(f"Creating a Board needs to have all {MAX_SCALE*MAX_SCALE} values\n{values}")
        board = np.empty(shape=(MAX_SCALE, MAX_SCALE))
        counter = 0

        for x in range(MAX_SCALE):
            for y in range(MAX_SCALE):
                dbg(f"x: {x}, y: {y}, counter: {counter}, value: {values[counter]}")
                if check_single_digit_int(values[counter]):
                    board[x, y] = values[counter]
                    counter += 1
        dbg(f"The Board,\n{board}")

    def edit_row(self, y_pos: int, values: [int]) -> None:
        # todo allow new row to start from certain column
        # todo for now allow 0, 0 etc
        # 0 implies keep original
        pass

    def edit_column(self, x_pos: int, values: [int]) -> None:
        pass

    def edit_single_tile(self, y_pos: int, x_pos: int, value: int) -> None:
        pass


valid_board_i = Board([2, 4, 8, 3, 9, 5, 7, 1, 6,
                       5, 7, 1, 6, 2, 8, 3, 4, 9,
                       9, 3, 6, 7, 4, 1, 5, 8, 2,
                       6, 8, 2, 5, 3, 9, 1, 7, 4,
                       3, 5, 9, 1, 7, 4, 6, 2, 8,
                       7, 1, 4, 8, 6, 2, 9, 5, 3,
                       8, 6, 3, 4, 1, 7, 2, 9, 5,
                       1, 9, 5, 2, 8, 6, 4, 3, 7,
                       4, 2, 7, 9, 5, 3, 8, 6, 1])

valid_board_j = Board([8, 2, 7, 1, 5, 4, 3, 9, 6,
                       9, 6, 5, 3, 2, 7, 1, 4, 8,
                       3, 4, 1, 6, 8, 9, 7, 5, 2,
                       5, 9, 3, 4, 6, 8, 2, 7, 1,
                       4, 7, 2, 5, 1, 3, 6, 8, 9,
                       6, 1, 8, 9, 7, 2, 4, 3, 5,
                       7, 8, 6, 2, 3, 5, 9, 1, 4,
                       1, 5, 4, 7, 9, 6, 8, 2, 3,
                       2, 3, 9, 8, 4, 1, 5, 6, 7])
