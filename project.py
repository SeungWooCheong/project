import random

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) 
    return None


def is_valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    numbers = list(range(1, 10))
    random.shuffle(numbers)  

    for num in numbers:
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


def generate_random_puzzle():
    board = [[0]*9 for _ in range(9)]
    solve(board) 

    empty_cells = 81 - random.randint(50, 60) 
    for _ in range(empty_cells):
        while True:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if board[row][col] != 0:
                board[row][col] = 0
                break
    return board

def solve_puzzle(board):
    solved_board = [row[:] for row in board] 
    solve(solved_board)  
    return solved_board

def is_board_full(board):
    for row in board:
        if 0 in row:
            return False
    return True

def get_user_input():
    while True:
        try:
            print("\nEnter row, column, and number to place (e.g., 'row column number'): ")
            user_input = input().strip().split()
            if len(user_input) != 3:
                raise ValueError("Please enter three values.")
            
            row = int(user_input[0]) - 1 
            col = int(user_input[1]) - 1  
            num = int(user_input[2])
            
            if not (1 <= row+1 <= 9 and 1 <= col+1 <= 9):
                raise ValueError("Row and column must be between 1 and 9.")
            
            if not (1 <= num <= 9):
                raise ValueError("Number must be between 1 and 9.")
            
            return (row, col, num)
        
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


if __name__ == "__main__":
    random.seed() 
    initial_board = generate_random_puzzle()
    solved_board = solve_puzzle(initial_board)

    print("Randomly Generated Sudoku Board:")
    print_board(initial_board)

    while not is_board_full(initial_board):
        row, col, num = get_user_input()

        if initial_board[row][col] == 0:
            if is_valid(initial_board, num, (row, col)):
                initial_board[row][col] = num
                print_board(initial_board)
            else:
                print(f"Invalid move! Please try again.")
        else:
            print("This cell is already filled. Please choose an empty cell.")

    if initial_board == solved_board:
        print("\nCongratulations! Sudoku puzzle solved!")
    else:
        print("\nOops! There seems to be an issue with the solution.")
