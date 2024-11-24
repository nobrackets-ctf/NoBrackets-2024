import random

FLAG = "NBCTF{C35t_1mp0rTan1_d3_54v01R_COmp1eR_jUsQu4_9}"

def print_board(sudoku_board):
    for row in sudoku_board:
        print(f'| {" | ".join(map(str, row))} |')


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
        puzzle_board[row][col] = "X"
    return puzzle_board

def banner():
    print("""
     .d8888b.                888          888                     .d8888b.            .d8888b.           
    d88P  Y88b               888          888                    d88P  "88b          d88P  Y88b          
    Y88b.                    888          888                    Y88b. d88P          888    888          
     "Y888b.   888  888  .d88888  .d88b.  888  888 888  888       "Y8888P"           888         .d88b.  
        "Y88b. 888  888 d88" 888 d88""88b 888 .88P 888  888      .d88P88K.d88P       888        d88""88b 
          "888 888  888 888  888 888  888 888888K  888  888      888"  Y888P"        888    888 888  888 
    Y88b  d88P Y88b 888 Y88b 888 Y88..88P 888 "88b Y88b 888      Y88b .d8888b        Y88b  d88P Y88..88P 
     "Y8888P"   "Y88888  "Y88888  "Y88P"  888  888  "Y88888       "Y8888P" Y88b       "Y8888P"   "Y88P"  
                                                                                                                                                                                                      
    """)

def format_envoi():
    sudoku_board = generate_sudoku()

    print("/!\ Informations concernant le format d'envoi de la solution !!")
    print("Veuillez envoyer votre solution en concaténant les nombres lignes par lignes.")
    print("Par exemple, vous avez trouvé la solution suivante :")
    print_board(sudoku_board)
    print(f"Le format d'envoi sera alors le suivant : {'-'.join(['-'.join(map(str, row))for row in sudoku_board])}")
    print("\n\n")

def parse_user_input(user_board):
    try : 
        x = user_board.split("-")
        board = []
        for i in range(0,len(x),9):
            board.append(list(map(int, x[i:i+9])))

        return board
    except Exception as e:
        print("Vous n'avez pas respecté le format !!")
        exit()

def is_user_board_ok(user_board, puzzle_board):
    valid = True
    for i in range(9):
        for j in range(9):
            if user_board[i][j] != puzzle_board[i][j]:
                valid = False
    return valid

banner()
format_envoi()

print("Arriveras-tu à résoudre tous mes sudokus ??")
for i in range(1,9):
    print(f"===== Step {i}/8 =====")
    # Generate a new Sudoku board
    sudoku_board = generate_sudoku()

    puzzle_board = create_puzzle_board(sudoku_board, blanks=i*5)
    print_board(puzzle_board)

    user_board = input("\nVotre solution >>")
    user_board = parse_user_input(user_board)

    if not is_user_board_ok(user_board, sudoku_board):
        print("Cette solution n'est pas valide. Recommence !!")
        exit()
    print("\n")

print(f"Félicitations !! Voici le flag : {FLAG}")
