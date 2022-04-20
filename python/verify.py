#!/usr/bin/python3
"""

"""
import board as bd


def verify_all(a_board: bd.Board, diag: bool) -> bool:
    """
    Run all the verification methods to validate if a sudoku solution is VALID!
    """
    if not verify_squares(a_board):
        return False
    if not verify_horizontals(a_board):
        return False
    if not verify_verticals(a_board):
        return False
    if diag:
        if not verify_diagonals(a_board):
            return False
    return True


def verify_squares(a_board: bd.Board) -> bool:
    """
    Verify all squares of a Board are VALID solutions
    """
    pass


def verify_horizontals(a_board: bd.Board) -> bool:
    """
    Verify all horizontals of a Board are VALID solutions
    """
    pass


def verify_verticals(a_board: bd.Board) -> bool:
    """
    Verify all verticals of a Board are VALID solutions
    """
    pass


def verify_diagonals(a_board: bd.Board) -> bool:
    """
    Verify both NW to SE and NE to SW diagonals VALID solutions
    """
    pass


def filter_args():
    pass


def main():
    # TODO args
    # point to file
    # type in values?
    pass



if __name__ == "__main__":
    main()