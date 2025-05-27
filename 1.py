import pandas as pd
df = pd.read_csv('students.csv')
print("Первые пять строк: ")
print(df.head()) # head() по умолчанию показывает 5 первых строк
print("")

print("Информация о данных:")
df.info()
print("")

print("Статистика:")
print(df.describe())

average_score = df['Score'].mean() # mean() вычисляет среднее арифметическое
print(f"Средний балл всех студентов: {average_score:.2f}")
print("")

group_counts = df['Group'].value_counts().reset_index() #форматирование для красоты
group_counts.columns = ['Группа', 'Количество']
print("\nКоличество студентов по группам:")
print(group_counts)
