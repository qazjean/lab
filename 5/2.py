import numpy as np
import matplotlib.pyplot as plt

# Генерация данных
data = np.random.normal(size=1000)  # По умолчанию: μ=0 (мат ожидание), σ=1 (отклонение)

# Создание гистограммы
plt.figure(figsize=(9, 5))
plt.hist(data, bins=20, color='pink', edgecolor='black')

# Оформление
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('result3.png', dpi=200, bbox_inches='tight')
# Показать график
plt.show()