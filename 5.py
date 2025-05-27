import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('students.csv')

# Гистограмма распределения баллов
fig1 =plt.figure(figsize=(12, 6))

plt.hist(df['Score'],
         bins=10,
         color='pink',
         edgecolor='black') #на 10 интервалов

plt.title('Распределение баллов студентов', fontsize=14)
plt.xlabel('Балл', fontsize=12)
plt.ylabel('Количество студентов', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout() #"подгоняет" расположение подписей осей, заголовков
plt.show()
fig1.savefig('score_histogram.png', dpi=300, bbox_inches='tight')
plt.close(fig1)



# Столбчатая диаграмма средних баллов по группам
fig2 = plt.figure(figsize=(12, 6))
group_scores = df.groupby('Group')['Score'].mean()
# Построение диаграммы
group_scores.plot(kind='bar',
                 color=['pink', 'lightblue', 'purple', 'orange'],
                 edgecolor='black')

plt.title('Средний балл по группам', fontsize=14)
plt.xlabel('Группа', fontsize=12)
plt.ylabel('Средний балл', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout() #"подгоняет" расположение подписей осей, заголовков
plt.show()
fig2.savefig('group_scores.png', dpi=300, bbox_inches='tight')
plt.close(fig2)