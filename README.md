# sudoku_verify

This is a simple Sudoku Board verifier script

## Requirements
Only Python3, its standard libraries and the Numpy Library are needed for this Verifier Script
```bash
python3 -m pip install numpy
# You may need to upgrade your pip
```
## Usage
This Script can be called directly or via the Python Consol
### Command Line
```Bash
cd sudoku_verify
python3 python/verify.py --example 1 --debug # VALID
python3 python/verify.py --example 2 # VALID
python3 python/verify.py --example 3 # INVALID
python3 python/verify.py --csv ???.csv
```
Tell the Verifier to run on either of 3 examples, example 3 is INVALID

### Python Console
```Bash
python3 # load python console
import board as bd
import verify
board_to_verify = bd.Board([2, 4, 8, 3, 9, 5, 7, 1, 6,
                            5, 7, 1, 6, 2, 8, 3, 4, 9,
                            9, 3, 6, 7, 4, 1, 5, 8, 2,
                            6, 8, 2, 5, 3, 9, 1, 7, 4,
                            3, 5, 9, 1, 7, 4, 6, 2, 8,
                            7, 1, 4, 8, 6, 2, 9, 5, 3,
                            8, 6, 3, 4, 1, 7, 2, 9, 5,
                            1, 9, 5, 2, 8, 6, 4, 3, 7,
                            4, 2, 7, 9, 5, 3, 8, 6, 1])
verify_board(board_to_verify, diag=False)
```
Import the board module and the verify module, then create a board of 81 values

Then verify the board using the catch all method. Or call the individual verification methods
```Bash
python3 # load python console
verify_squares(board_to_verify)
verify_rows(board_to_verify)
verify_columns(board_to_verify)
```
You can also edit a Board once its been made, see board.py for more information
## Improvements
- Allow editing of row or column to start from within column or row and not always from beginning
- Allow creation of new board with "holes" if you want to replace large areas of the board
- Have single method to check values are ints and between 0-9 or 1-9 etc
- ~~Add an INVALID example~~
- Add Diagonal verification