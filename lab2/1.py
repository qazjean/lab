f = open("data.txt")
a = [int(f.readline()) for i in range(10)]
print(sum(a), sum(a)/10, max(a), min(a))
t = open("result.txt", "w",encoding='utf-8') #файл с результатами
t.write(f"Сумма: {sum(a)}\n")
t.write(f"Среднее: {sum(a)/10}\n")
t.write(f"Максимум: {max(a)}\n")
t.write(f"Минимум: {min(a)}\n")
f.close()
t.close()