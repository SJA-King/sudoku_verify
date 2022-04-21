#!/usr/bin/python3
"""
This Script acts as the module for a 9x9 Board of 81 integers representing a Sudoku board

A Board can be created via a python console or via another script using this one as a module
"""
import logging
import numpy as np
from typing import List

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
    logging.debug(msg)


class Board:
    """
    A Board is made up of 9x9 "tiles"
    """
    the_board = None

    def __init__(self, values: List):
        if len(values) != MAX_SCALE*MAX_SCALE:
            raise Exception(f"Creating a Board needs to have all {MAX_SCALE*MAX_SCALE} values!\n{values}")
        self.the_board = np.empty(shape=(MAX_SCALE, MAX_SCALE))
        counter = 0

        for x in range(MAX_SCALE):
            for y in range(MAX_SCALE):
                dbg(f"x: {x}, y: {y}, counter: {counter}, value: {values[counter]}")
                if check_single_digit_int(values[counter]):
                    self.the_board[x, y] = values[counter]
                    counter += 1
        dbg(f"The Board,\n{self.the_board}")

    def edit_row(self, y_pos: int, values: [int]) -> None:
        """
        Allow a user to update a row of the Sudoku Board
        """
        if len(values) != MAX_SCALE:
            raise Exception(f"Editing a Row needs {MAX_SCALE} values!\n{values}")
        counter = 0
        for x in range(MAX_SCALE):
            self.the_board[x, y_pos] = values[counter]
            counter += 1

    def edit_column(self, x_pos: int, values: [int]) -> None:
        """
        Allow a user to update a column of the Sudoku Board
        """
        if len(values) != MAX_SCALE:
            raise Exception(f"Editing a Column needs {MAX_SCALE} values!\n{values}")
        counter = 0
        for y in range(MAX_SCALE):
            self.the_board[x_pos, y] = values[counter]
            counter += 1

    def set_tile(self, y_pos: int, x_pos: int, value: int) -> None:
        """
        Allow a user to set a single tile of the Sudoku Board
        """
        if check_single_digit_int(value):
            self.the_board[x_pos, y_pos] = value

    def display(self):
        """
        Print the entire Board
        """
        print(self.the_board)

    def get_tile(self, y_pos: int, x_pos: int) -> int:
        """
        Getter for a single tile
        """
        return self.the_board[x_pos, y_pos]



