import numpy as np
import matplotlib.pyplot as plt

# Создаем фигуру с 3 вертикальными областями
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10))  #у меня они в три строки

#Линейный график y = x²
x = np.linspace(-5, 5, 100)
ax1.plot(x, x**2, color='purple', linewidth=2)
ax1.set_title('Линейный график: y = x²')
ax1.set_xlabel('Ось X')
ax1.set_ylabel('Ось Y')
ax1.grid(True, linestyle='--')

#График 2: Точечный график
x_points = np.random.uniform(0, 10, size=50)  # Дробные числа [0, 10)
y_points = np.random.uniform(0, 5, size=50)
ax2.scatter(x_points, y_points,
            color='blue',
            edgecolor='black',
            s=40,  # Размер точек
)
ax2.set_title('Случайные точки')
ax2.set_xlabel('X координата')
ax2.set_ylabel('Y координата')
ax2.grid(True, linestyle=':')

#График 3: Столбчатая диаграмма
categories = ['hihi', 'haha', 'hahi']
values = np.random.randint(1, 11, size=3)
bars = ax3.bar(categories,
               values,
               color=['pink', 'lightblue', 'purple'],
               edgecolor='black',
               width=0.5)

ax3.set_title('Категориальные данные')
ax3.set_ylabel('Значения')
ax3.grid(axis='y')

# Добавляем значения на столбцы
for bar in bars: #проходим по всем столбцам
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2.,
             height + 0.2,
             f'{height}',
             ha='center',
             va='bottom')
 #половина ширины столбца и небольшой отступ от границы
# Настраиваем отступы между графиками
plt.tight_layout(pad=4.0)
plt.savefig('result5.png', dpi=200, bbox_inches='tight')
# Показать
plt.show()

