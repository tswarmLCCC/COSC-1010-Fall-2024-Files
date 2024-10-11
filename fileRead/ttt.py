import random


def display_board(board):
    """Displays the current Tic Tac Toe board in a user-friendly format."""
    for row in board:
        print(" ".join(row))


def is_winner(board, player):
    """Checks if the given player has achieved a winning condition."""
    win_conditions = ((0, 0, 0), (1, 1, 1), (2, 2, 2),
                      (0, 1, 2), (1, 2, 0), (0, 2, 1),
                      (2, 1, 0), (1, 0, 2))
    for condition in win_conditions:
        if board[condition[0]][condition[1]] == player and \
           board[condition[1]][condition[2]] == player and \
           board[condition[2]][condition[0]] == player:
            return True
    return False


def is_board_full(board):
    """Checks if all squares on the board are occupied."""
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def get_player_move(board, player):
    """Gets the valid player move (row, column)."""
    move = input(f"Player {player}, enter your move (row, column): ")
    while True:
        try:
            row, col = move.split(',')
            row = int(row) - 1
            col = int(col) - 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Please enter an empty square (1-3, 1-3).")
        except ValueError:
            print("Invalid input. Please enter a comma-separated pair of numbers.")
        move = input("Try again: ")


def ai_move(board):
    """Implements AI logic to make a strategic move."""
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'  # Simulate O's move
                if is_winner(board, 'O'):
                    board[i][j] = ' '  # Undo the move
                    return i, j  # AI wins by placing O here
                board[i][j] = ' '  # Simulate X's move
                if is_winner(board, 'X'):
                    board[i][j] = ' '  # Undo the move
                    return i, j  # Prevent X from winning immediately
                board[i][j] = ' '  # Undo both moves

    # If AI can't win or block an immediate X win, choose a random empty square
    empty_squares = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_squares.append((i, j))
    return random.choice(empty_squares)


def play_game():
    """Main game loop."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = random.choice(['X', 'O'])  # Randomly choose starting player

    while True:
        # Check for immediate win for any player
        if is_winner(board, 'X') or is_winner(board, 'O'):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        display_board(board)

        if current_player == 'X':
            row, col = get_player_move(board, current_player)
        else:
            row, col = ai_move(board)  # AI move

        board[row][col] = current_player

        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_game()
