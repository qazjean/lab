import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных
data = np.genfromtxt('data.csv', delimiter=',', skip_header=1) #1ая строка - заголовок

# Извлечение нужных столбцов
# первый столбец (индекс 0) - X, второй (индекс 1) - Y
x = data[:, 0] # Все строки, первый столбец
y = data[:, 1]

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'pink', linewidth=2, label='Зависимость Y(X)')
plt.title('График зависимости из файла data.csv', fontsize=14)
plt.xlabel('X-ось', fontsize=12)
plt.ylabel('Y-ось', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.savefig('result7.png', dpi=200, bbox_inches='tight')
# Показать график
plt.show()