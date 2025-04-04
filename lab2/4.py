import re
a = open("text.txt", encoding='utf-8').read()
emails = re.findall(r'[a-zA-Z0-9*&._+%-]+@[a-zA-Z]+\.[a-zA-Z]{2,4}', a)
phones = re.findall(r'\+7-\d{3}-\d{3}-\d{2}-\d{2}', a)
capital_words = re.findall(r'\b[A-ZА-ЯЁ][a-zа-яё]*\b', a)
t1 = open("emails.txt", "w", encoding='utf-8')
for email in emails:
    t1.write(email + '\n')
t2 = open("phones.txt", "w", encoding='utf-8')
for phone in phones:
    t2.write(phone + '\n')
t3 = open("capital_words.txt", "w", encoding='utf-8')
for word in capital_words:
    t3.write(word + '\n')
t1.close()
t2.close()
t3.close()