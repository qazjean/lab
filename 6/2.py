import pandas as pd
df = pd.read_csv('students.csv')
hight_scores = df[df["Score"]>80].sort_values("Score", ascending=False) #по убыванию балла
print("Студенты с баллом выше 80")
print(hight_scores)
print("")
staric = df.loc[df["Age"].idxmax()]
mladenez = df.loc[df["Age"].idxmin()]
print(f"Самый старший студент: {staric['Name']}. Его возраст: {staric['Age']}")
print(f"Самый молодой студент: {mladenez['Name']}. Его возраст: {mladenez['Age']}")