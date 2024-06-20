import random

def print_board(board): # 보드를 생성
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
                return (i, j) # (row, column)
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

    for nu경
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
