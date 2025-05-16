import numpy as np

# Создание матрицы 5x5
matrix = np.random.randint(1, 11, size=(5, 5))
print("Исходная матрица:")
for i in matrix:
    print(i)

mean_value = np.mean(matrix)
max_value = np.max(matrix)
min_value = np.min(matrix)
column_sums = np.sum(matrix, axis=0) #cумма по столбцам

# Вывод результатов
print("\n1. Среднее значение матрицы:", mean_value)
print("2. Максимальный элемент:", max_value)
print("3. Минимальный элемент:", min_value)
print("4. Суммы по столбцам:")
print(column_sums)