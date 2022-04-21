#!/usr/bin/python3
"""

"""
import argparse
import board as bd
import logging

NUMBERS = set(range(1, 10))


def verify_board(a_board: bd.Board, diag: bool):
    """
    Run all the verification methods to validate if a sudoku solution is VALID!
    """
    board_valid = True
    verify_methods = [verify_squares(a_board),
                      verify_rows(a_board),
                      verify_columns(a_board)]
    if diag:
        verify_methods.append(verify_diagonals(a_board))

    for v_method in verify_methods:
        if not v_method:
            board_valid = False

    if board_valid:
        print("Board is a VALID Solution!")
        logging.info(a_board)
    else:
        print(f"Board is an INVALID Solution!")


def verify_squares(a_board: bd.Board) -> (bool, [str]):
    """
    Verify all squares of a Board are VALID solutions
    """
    all_squares_valid = True
    invalid_squares = []

    #0-2 - 0-2, 3-5, 6-8
    #3-5 - 0-2, 3-5, 6-8
    #6-8 - 0-2, 3-5, 6-8

    return all_squares_valid, invalid_squares


def verify_rows(a_board: bd.Board) -> (bool, [str]):
    """
    Verify all rows of a Board are VALID solutions
    """
    all_rows_valid = True
    for row in range(bd.MAX_SCALE):
        row_valid = False
        this_row = []
        for col in range(bd.MAX_SCALE):
            this_row.append(a_board.get_tile_value(col, row))

        if NUMBERS == set(this_row):
            row_valid = True
            bd.info(f"row: {row}, {this_row}, Valid: {row_valid}")
        else:
            all_rows_valid = False
            print(f"row: {row}, {this_row}, Valid: {row_valid}")
    return all_rows_valid


def verify_columns(a_board: bd.Board) -> (bool, [str]):
    """
    Verify all columns of a Board are VALID solutions
    """
    all_columns_valid = True
    for col in range(bd.MAX_SCALE):
        column_valid = False
        this_column = []
        for row in range(bd.MAX_SCALE):
            this_column.append(a_board.get_tile_value(col, row))

        if set(NUMBERS) == set(this_column):
            column_valid = True
            bd.info(f"column: {col}, {this_column}, Valid: {column_valid}")
        else:
            all_columns_valid = False
            print(f"column: {col}, {this_column}, Valid: {column_valid}")
    return all_columns_valid


def verify_diagonals(a_board: bd.Board) -> bool:
    """
    Verify both NW to SE and NE to SW diagonals VALID solutions
    """
    pass


def args_parser():
    parser = argparse.ArgumentParser(
        description='')
    parser.add_argument('--debug', help='Enable Debug Output', action='store_true')
    parser.add_argument('--info', help='Enable Info Output', action='store_true')
    parser.add_argument('--csv', help='Point to a csv file with 81 values', type=str)
    parser.add_argument('--example', help='Run an example: 1, 2', type=int)

    args = parser.parse_args()

    if args.debug:
        level = logging.DEBUG
        logging.basicConfig(level=level, format='[%(levelname)s] - %(message)s')
        logging.debug(f"Args: {args}")
    if args.info:
        level = logging.INFO
        logging.basicConfig(level=level, format='[%(levelname)s] - %(message)s')

    return args


def main():
    args = args_parser()

    board_to_verify = None
    if args.csv:
        import csv
        values = []
        with open(args.csv, 'r') as file:
            rows = list(csv.reader(file))

        for row in rows:
            for i_r in row:
                values.append(int(i_r))
        bd.dbg(str(values))
        board_to_verify = bd.Board(values)
    elif args.example:
        if args.example == 1:
            board_to_verify = bd.Board([2, 4, 8, 3, 9, 5, 7, 1, 6,
                                        5, 7, 1, 6, 2, 8, 3, 4, 9,
                                        9, 3, 6, 7, 4, 1, 5, 8, 2,
                                        6, 8, 2, 5, 3, 9, 1, 7, 4,
                                        3, 5, 9, 1, 7, 4, 6, 2, 8,
                                        7, 1, 4, 8, 6, 2, 9, 5, 3,
                                        8, 6, 3, 4, 1, 7, 2, 9, 5,
                                        1, 9, 5, 2, 8, 6, 4, 3, 7,
                                        4, 2, 7, 9, 5, 3, 8, 6, 1])
        elif args.example == 2:
            board_to_verify = bd.Board([8, 2, 7, 1, 5, 4, 3, 9, 6,
                                        9, 6, 5, 3, 2, 7, 1, 4, 8,
                                        3, 4, 1, 6, 8, 9, 7, 5, 2,
                                        5, 9, 3, 4, 6, 8, 2, 7, 1,
                                        4, 7, 2, 5, 1, 3, 6, 8, 9,
                                        6, 1, 8, 9, 7, 2, 4, 3, 5,
                                        7, 8, 6, 2, 3, 5, 9, 1, 4,
                                        1, 5, 4, 7, 9, 6, 8, 2, 3,
                                        2, 3, 9, 8, 4, 1, 5, 6, 7])
        else:
            raise Exception(f"Must denote example number, {args.example}")
    else:
        raise Exception("Must denote if this file is running with a file or the examples")

    # verify_rows(board_to_verify)
    # verify_columns(board_to_verify)
    verify_squares(board_to_verify)

    # verify_all(board_to_verify, diag=False)


if __name__ == "__main__":
    main()
