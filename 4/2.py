import random
class Card: #класс карты. Сюда можно было бы определить плучение значения для дам и тд, но в упрощенной версии этого нет)
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"{self.rank}"

class Deck:  #класс для "колоды" ( по факту - рандомное число
    def shuffle(self):
        return random.randint(2, 11)


class Hand: #класс для "карт в руках"
    def __init__(self):
        self.value = 0

    def add_card(self, card):
        self.value += card


class Chips: #класс для фишек (в начале их 100, но пользователь может выиграть/проиграть)
    def __init__(self):
        try:
            with open("chips.txt") as f:
                self.total = int(f.read())
        except:
            self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
    def save_chips(self):
        with open("chips.txt", "w") as f:
            f.write(str(self.total))


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Сколько фишек вы хотите поставить? "))
        except ValueError:
            print("Пожалуйста, введите число!")
        else:
            if chips.bet > chips.total:
                print(f"У вас недостаточно фишек! Доступно: {chips.total}")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.shuffle())


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Берёте ещё или останавливаетесь? Введите 'да' или 'нет': ").lower()
        if x == 'да':
            hit(deck, hand)
        elif x == 'нет':
            print("Игрок останавливается. Ход дилера.")
            playing = False
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")
            continue
        break



def show_some(player):  #тк во время игры игрок не видит очки сопернкика
    print("Очки игрока:", player.value)


def show_all(player, dealer):
    print("Очки дилера:", dealer.value)
    print("Очки игрока:", player.value)


def player_loose(chips):
    print("Игрок проиграл!")
    chips.lose_bet()


def player_wins(chips):
    print("Игрок выиграл!")
    chips.win_bet()

def push():
    print("Ничья! Фишки возвращаются.")

def main():
    global playing

    print("Игра в Блэкджек!")

    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    # Раздаём по две карты
    player_hand.add_card(deck.shuffle())
    player_hand.add_card(deck.shuffle())
    dealer_hand.add_card(deck.shuffle())
    dealer_hand.add_card(deck.shuffle())

    # Создаём фишки игрока
    player_chips = Chips()
    # Делаем ставки
    take_bet(player_chips)

    show_some(player_hand)

    playing = True

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand)

        if player_hand.value > 21:
            player_loose(player_chips)
            break

    if player_hand.value <= 21:
        # Дилер берёт карты, пока не наберёт 17 или больше
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        # Проверяем исход игры
        if dealer_hand.value > 21 or dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        elif dealer_hand.value > player_hand.value:
            player_loose(player_chips)
        else:
            push()

    # Показываем общее количество фишек
    print(f"\nУ игрока осталось фишек: {player_chips.total}")
    player_chips.save_chips()
main()
