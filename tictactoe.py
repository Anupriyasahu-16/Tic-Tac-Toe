def print_board(board):
    """
    Prints the tic-tac-toe board.
    """
    print("---------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" ")
        print("|")
    print("---------")


def initialize_board():
    """
    Initializes an empty tic-tac-toe board.
    """
    return [[" " for _ in range(3)] for _ in range(3)]


def is_board_full(board):
    """
    Checks if the board is full.
    """
    for row in board:
        if " " in row:
            return False
    return True


def is_winner(board, player):
    """
    Checks if the specified player has won.
    """
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def make_move(board, row, col, player):
    """
    Makes a move on the board.
    """
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        return False


def play_game():
    """
    Plays a game of tic-tac-toe.
    """
    board = initialize_board()
    current_player = "X"

    while True:
        print_board(board)

        if is_winner(board, "X"):
            print("Player X wins!")
            break
        elif is_winner(board, "O"):
            print("Player O wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if make_move(board, row, col, current_player):
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        else:
            print("Invalid move. Try again.")

    print_board(board)


# Start the game
play_game()
