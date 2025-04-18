class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Приватный атрибут

    @property
    def celsius(self): #геттер
        return self._celsius

    @celsius.setter
    def celsius(self, value):  #сеттер с валидацией (число ли)
        if not isinstance(value, (int, float)):
            raise TypeError("Температура должна быть числом")
        self._celsius = value

    @property
    def fahrenheit(self): #перевод в фаренгейты (геттер)
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value): #cеттер для температуры в Фаренгейтах с валидацией
        if not isinstance(value, (int, float)):
            raise TypeError("Температура должна быть числом")
        self._celsius = (value - 32) * 5 / 9  #перевод в градусы по цельсию

    def __str__(self):
        return f"{self._celsius:.1f}°C ({self.fahrenheit:.1f}°F)"

# Пример использования
if __name__ == "__main__":
    temp = Temperature(20)
    print(temp)  #строковое представление через __str__

    # Работа с celsius через геттер property
    temp.celsius = 20
    print(f"Цельсии: {temp.celsius}")
    print(f"Фаренгейты: {temp.fahrenheit}")

    # Установка температуры через Фаренгейты (сеттер)
    temp.fahrenheit = 100
    print(temp) #строковое представление через __str__

    # Проверка валидации
    try:
        temp.fahrenheit = "холодно"  # Вызовет TypeError
    except TypeError as e:
        print(f"Ошибка: {e}")
