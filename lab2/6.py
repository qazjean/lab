import re
from datetime import datetime
def change_data(a):
    with open(a, encoding='utf-8') as f:
        t = f.read()
    data = re.findall(r'\b(\d{2})\.(\d{2})\.(\d{4})\b', t)
    res = [] #сюда сохраним измененые даты
    for d, m, year in data:
        if 1<= int(d) <= 31 and 1 <= int(m) <= 12:
            changed = f"{year}-{m}-{d}"
            res.append(changed)
    res.sort(key = lambda d: datetime.strptime(d, "%Y-%m-%d")) #сортируем с помощью метода strptime
    #класса datetime
    return res
res = change_data("text.txt")
r = open("dates.txt", "w", encoding='utf-8')
for d in res:
    r.write(d + '\n')
    print(d)
r.close()