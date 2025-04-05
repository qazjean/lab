import csv
from student_utils import get_top_students, get_average_age, filter_students_by_grade

with open('students.csv', encoding='utf-8') as f:
    students = list(csv.DictReader(f)) #данные об учениках (в списке)
    for s in students:
        s['Возраст'] = int(s['Возраст'])
        s['Средний балл'] = float(s['Средний балл'])

# Используем ранее созданные методы
top_students = get_top_students(students, 4) #к тпримеру, мы хотим топ 4 студента
average_age = get_average_age(students)
filtered_students = filter_students_by_grade(students, 4.5) #и балл выше 4.5 хотим

# Сортируем по возрасту
sorted_by_age = sorted(students, key=lambda x: x['Возраст'])

# Сохраняю в report.txt(для удобства отделила пустой строкой разные части ответа)
with open('report.txt', 'w', encoding='utf-8') as t:
    t.write('Топ-4 студента:\n')
    for student in top_students:
        t.write(f"Имя: {student['Имя']}, Возраст: {student['Возраст']}, Средний балл: {student['Средний балл']}\n")

    t.write(f'\nСредний возраст студентов: {average_age:.2f}\n')

    t.write('\nСтуденты с средним баллом выше 4.5:\n')
    for student in filtered_students:
        t.write(f"Имя: {student['Имя']}, Возраст: {student['Возраст']}, Средний балл: {student['Средний балл']}\n")

    t.write('\nСтуденты отсортированные по возрасту:\n')
    for student in sorted_by_age:
        t.write(f"Имя: {student['Имя']}, Возраст: {student['Возраст']}, Средний балл: {student['Средний балл']}\n")
#решено
