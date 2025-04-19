import random
import datetime
class Game():
    def __init__(self, number):
        self.number = number
        self.time = datetime.datetime.now()
        self.count = 0
    def trying(self):
        log = Log()
        while True:
            y = int(input("Введите ваше число: "))
            self.count += 1
            if y != self.number:

                if y < self.number:
                    print("Ваше число меньше")
                    log.logging(self.count, y,"Меньше")
                else:
                    print("Ваше число больше")
                    log.logging(self.count, y, "Больше")
            else:
                break
        log.logging(self.count, y,"Угадали")
        print("Угадали")
    def show(self):
        print(f"Вы угадали за {datetime.datetime.now() - self.time}")
        print(f"Вам понадобилось {self.count} попытки (ок)")


class Log():
    def __init__(self):
        self.log = open("log.txt", "w", encoding='utf-8')
    def logging(self, num_try, num, bm):
        self.num_try = num_try
        self.num = num
        self.bm = bm
        self.log.write(f"Номер попытки: {self.num_try}, Ваше число: {self.num}, Статус: {self.bm}, Время попытки: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} \n")



c = random.randint(1, 10)
t = Game(c)
t.trying()
t.show()
