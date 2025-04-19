import subprocess
import sys
def Choose():
    print("В какую игру вы хотите поиграть? 1 - Угадай число, 2 - Блекджек, 3 - Крестики-нолик, 4 - Я больше не хочу играть")


def run_game(game_file):
    subprocess.run([sys.executable, game_file])

def main():
    while True:
        Choose()
        t = input("Введите номер:")
        if t == '1':
            run_game("1.py")
        elif t == '2':
            run_game("2.py")
        elif t == '3':
            run_game("4withcomputer.py")
        elif t == "4":
            print("Спасибо за игру!")
            break
        else:
            print("Такой игры у нас нет, попробуйте еще раз")

if __name__ == "__main__":
    main()
