import pandas as pd

df = pd.read_csv('students.csv')

df['Passed'] = (df['Score'] >= 60).astype(int) #1, если балл больше равен 60 (astype(int) из T/F делает 1,0)


group_stats = df.groupby('Group').agg(
    Average_Score=('Score', 'mean'),
    Median_Age=('Age', 'median')
).reset_index() #благодаря reset_index Group превратился в обычный столбец.
print("Статистика по группам:")
print(group_stats.to_string(index=False))

print("\nПервые 5 строк с новым столбцом Passed:")
print(df.head().to_string(index=False))

