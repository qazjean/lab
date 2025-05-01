def print_board(board):
    for i in range(3):
        print(f"{board[i*3]} | {board[i*3 + 1]} | {board[i*3 + 2]} ")
        if i < 2:
            print("--------------")

def check_winner(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]

    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]

    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    if " " not in board:
        return "Ничья"
    return None

def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"

    while True:
        print_board(board)
        print(f"\nХод игрока {current_player}")

        try:
            move = int(input("Выберите клетку (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Пожалуйста, введите число от 1 до 9.")
                continue
        except ValueError:
            print("Пожалуйста, введите число.")
            continue

        if board[move] != " ":
            print("Эта клетка уже занята!")
            continue

        board[move] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            if winner == "Ничья":
                print("Мир, дружба, жвачка")
            else:
                print(f"Игра окончена! Победил {winner}")
                break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
