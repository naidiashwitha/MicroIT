def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False

def check_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

def tic_tac_toe():
    board = ['1','2','3','4','5','6','7','8','9']
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if board[move] in ['X', 'O']:
                print("That spot is already taken. Try again.")
                continue
            board[move] = current_player
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")
            continue

        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            game_over = True
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
