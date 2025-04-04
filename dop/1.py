import re

with open('server_logs.txt', 'r',  encoding='utf-8') as file:
    t = file.read()
logs = re.findall(r'\[(.*?)] \[(.*?)] \[(.*?)] \[(.*?)] \[(.*?)] \[(.*?)] \[(.*?)]', t)
# сразу разделяем и сохраняем в список
s200, data_size = 0, 0
uip = set()

#ведем подсчеты
for log in logs:
    date, time, ip, method, url, status, size = log
    if status == '200':
        s200 += 1
    data_size += int(size)
    uip.add(ip)

# Сохраняем результаты
with open('log_analysis.txt', 'w', encoding='utf-8') as res:
    res.write(f'Количество запросов с кодом статуса 200: {s200}\n')
    res.write(f'Общий объём данных, переданных сервером: {data_size} байт\n')
    res.write(f'Количество уникальных IP-адресов: {len(uip)}\n')

# Сортируем по дате и времени
logs.sort(key=lambda x: (x[0], x[1]))

for log in logs[:10]:
    print(log)

