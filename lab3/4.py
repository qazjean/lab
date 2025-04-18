import datetime  # Для записи времени транзакций

class BankAccount:
    def __init__(self, initial_balance=0): #Инициализация банковского счета, начальный баланс счета по умолчанию 0
        self._balance = initial_balance  # Приватный атрибут для хранения баланса
        self._transactions = []  # Приватный список для хранения истории операций
        self._log_transaction("Account opened", initial_balance)  # Логируем создание счета, метод описан ниже

    def deposit(self, amount): #Пополнение счета.
        if amount <= 0:
            raise ValueError("Размер депозита не может быть отрицательным")
        self._balance += amount
        self._log_transaction("Deposit", amount) #логируем (этот метод ниже)

    def withdraw(self, amount): #снятие со счета
        if amount <= 0:
            raise ValueError("Размер снятия не может быть отрицательным")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount
        self._log_transaction("Withdrawal", -amount) #логируем

    def _log_transaction(self, operation, amount): #Приватный! метод для логирования операций. Сохраняет информацию в формате словаря
        transaction = {
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), #время
            'operation': operation, #пополнение или снятие
            'amount': amount,
            'balance': self._balance #Приватный атрибут
        }
        self._transactions.append(transaction)

    @property
    def balance(self): #геттер для получения баланса. Позволяет оставить баланс приватным атрибутом И использовать
        #balance как атрибут, а не метод
        return self._balance

    def print_transactions(self): #Печатает выписку по счету с историей операций (этот метод публичный, он не изменяет transactions)
        print("\nTransaction History:")
        for tx in self._transactions:
            print(f"{tx['date']} | {tx['operation']:15} | " #:15 для выравнивания, 9.2f тоже (ну .2 для двух знаков после запятой)
                  f"{(tx['amount']):9.2f} | "
                  f"Balance: {tx['balance']:.2f}")


# Пример
if __name__ == "__main__":
    # Создаем новый счет с балансом 1000000
    account = BankAccount(1000000)
    # Выполняем операции
    try:
        account.deposit(500) #добавим 500
        account.withdraw(1) #снимем рубль
        account.withdraw(500000000000000)  # Вызовет ошибку
    except ValueError as e:
        print(f"Error: {e}") #чтобы эта ошибка не ломала код

    # Печатаем информацию о транзакциях (используем публичный метод)
    account.print_transactions()

    # Получаем текущий баланс через геттер property
    print(f"\nCurrent balance: {account.balance:.2f}") #2f для двух знаков после запятой
