import random
from pwn import *
import time

def is_valid(board, row, col, num):
    # Check the row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def fill_board(board):
    # Try to find an empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try numbers 1-9 in the empty cell
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if fill_board(board):
                            return True
                        board[row][col] = 0  # Reset cell
                return False
    return True

def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    fill_board(board)
    return board

def create_puzzle_board(board, blanks=40):
    # Make a copy of the board
    puzzle_board = [row[:] for row in board]
    # Randomly remove values to create blanks
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    for i in range(blanks):
        row, col = cells[i]
        puzzle_board[row][col] = 0
    return puzzle_board

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Reset cell if not solvable
                return False  # Trigger backtracking
    return True  # Board solved


def get_puzzle():
    r.recvuntil(b"/8 =====\n")
    puzzle = r.recvuntil(b"\n\n").strip().decode()
    puzzle = [list(map(int, row.strip(" |").split(" | "))) for row in puzzle.split("\n")]
    
    return puzzle


def send_puzzle(board):
    r.recvuntil(b"solution >>")

    solution = '-'.join(['-'.join(map(str, row))for row in board])
    r.sendline(solution.encode())

r = remote("localhost", 1337)

for _ in range(8):
    time.sleep(1)
    print(f"Tour {_+1}/8")
    puzzle_board = get_puzzle()

    solve_sudoku(puzzle_board)
    print(f"Solution trouvée : {puzzle_board}")
    solution_board = puzzle_board
    send_puzzle(solution_board)

result = r.recv()
if b"Recommence" in result:
    print("Erreur tour 8")
else:
    print(result.decode())