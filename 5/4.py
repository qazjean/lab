import numpy as np
import matplotlib.pyplot as plt

matrix = np.random.randint(1, 11, size=(5, 5))  #матрица как в прошлой задаче

# Создаем фигуру
plt.figure(figsize=(8, 6))

# Построение тепловой карты
heatmap = plt.imshow(matrix)  #imshow() отображает матрицу как изображение

# Добавление colorbar (шкала соответствия цветов и чисел)
cbar = plt.colorbar(heatmap)

cbar.set_label('Значения', rotation=270, labelpad=15) #надпись справа, так что я ее повернула

# Добавление значений (проходя по всем элементам. matrix.shape[0] — количество строк.)
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        text_color = 'black'
        plt.text(j, i, matrix[i, j],
                 ha='center', va='center',
                 color=text_color,
                 fontsize=12) #вставляем значение

# Настройки отображения
plt.title('Тепловая карта матрицы 5x5')
plt.xlabel('Столбцы')
plt.ylabel('Строки')
plt.savefig('result4.png', dpi=200, bbox_inches='tight')
plt.show()