def get_top_students(students, n):
    return sorted(students, key=lambda x: x['Средний балл'], reverse=True)[:n]

def get_average_age(students):
    total_age = sum(s['Возраст'] for s in students)
    try:
        return total_age / len(students)
    except:
        return 0
def filter_students_by_grade(students, min_grade):
    return [s for s in students if s['Средний балл'] > min_grade]
