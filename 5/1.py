import numpy as np
import matplotlib.pyplot as plt
# Создание массива x
x = np.linspace(0, 10, 100)

# Вычисление значений функций
y = np.sin(x)
z = np.cos(x)

# Создание графика
plt.figure(figsize=(9, 6))  # Размер графика (не обзательно, но мне понравилось так)

# Построение графиков
plt.plot(x, y, label='sin(x)', color='pink')    # График синуса
plt.plot(x, z, label='cos(x)', color='lightblue')     # График косинуса

plt.title('Графики функций sin(x) и cos(x)')    # Заголовок
plt.xlabel('x')                                 # Подпись оси X
plt.ylabel('y')                                 # Подпись оси Y
plt.grid(True)                                  # Включение сетки
plt.legend()                                    # Отображение легенды
plt.savefig('result1.png', dpi=200, bbox_inches='tight')
# Показать
plt.show()