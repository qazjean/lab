import random


def print_board(board):
    for i in range(3):
        print(f" {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} ")
        if i < 2:
            print("-----------")


def check_winner(board):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return board[i]

    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return board[i]

    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]

    if " " not in board:
        return "Ничья"

    return None


def computer_move(board, computer_char):
    for i in range(9):
        if board[i] == " ":
            board[i] = computer_char
            if check_winner(board) == computer_char:
                return
            board[i] = " "

    player_char = "X" if computer_char == "O" else "O"
    for i in range(9):
        if board[i] == " ":
            board[i] = player_char
            if check_winner(board) == player_char:
                board[i] = computer_char
                return
            board[i] = " "

    if board[4] == " ":
        board[4] = computer_char
        return

    corners = [0, 2, 6, 8] #если не в центр, то вроде логичнее всего пойти в один из углов
    random.shuffle(corners)
    for i in corners:
        if board[i] == " ":
            board[i] = computer_char
            return

    for i in range(9):
        if board[i] == " ":
            board[i] = computer_char
            return


def play_game():
    board = [" "] * 9
    current_player = "X"

    choice = input("Вы хотите играть X или O? (X ходит первым): ").upper()
    while choice not in ["X", "O"]:
        choice = input("Пожалуйста, введите X или O: ").upper()

    player_char = choice
    computer_char = "O" if player_char == "X" else "X"

    if player_char == "X":
        print("Вы ходите первым (X)!")
    else:
        print("Компьютер ходит первым (X)!")
        current_player = "X"

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == "Ничья":
                print("Ничья!")
            else:
                print(f"Победили {winner}!")
            break

        if current_player == player_char:
            try:
                move = int(input("Ваш ход (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Пожалуйста, введите число от 1 до 9.")
                    continue
                if board[move] != " ":
                    print("Эта клетка уже занята!")
                    continue
                board[move] = player_char
                current_player = computer_char
            except ValueError:
                print("Пожалуйста, введите число от 1 до 9.")
        else:
            print("Секунду")
            computer_move(board, computer_char)
            current_player = player_char


print("Добро пожаловать в крестики-нолики!")
print("Позиции на поле:")
print(" 1 | 2 | 3 ")
print("-----------")
print(" 4 | 5 | 6 ")
print("-----------")
print(" 7 | 8 | 9 ")
print()

play_game()
