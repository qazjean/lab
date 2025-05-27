import pandas as pd

df = pd.read_csv('students.csv')

print("Количество пропусков по столбцам:")
print(df.isnull().sum())

#Заполнение пропусков в Score средним значением (zap)
zap = df['Score'].mean()
df['Score'] = df['Score'].fillna(zap)


df = df.dropna(subset=['Group']) #удалить пропуски только! в группах


print(f"Осталось строк: {len(df)}")
print(df)