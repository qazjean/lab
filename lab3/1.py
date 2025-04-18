class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    def add_grade(self, grade):
        if 0 <= grade <= 10: #на всякий случай проверим 
            self.grades.append(grade)
        else:
            print(f"oh! оценки {grade} нет")
    def get_average(self):
        if len(self.grades) > 0: #если оценок нет, то среднее значение 0
            return sum(self.grades)/len(self.grades)
        return 0.0
    def display_info(self): #красиво (на мой взгляд) вывожу информацию о студентах
        print(f"Имя студента: {self.name}")
        print(f"id студента: {self.student_id}")
        print(f"Его средний балл: {self.get_average()}")
        print(f"Оценки: {', '.join(map(str, self.grades))}")
if __name__ == "__main__":  # пример
    student = Student("Лизочка Пронина", "1511") #опробуем
    student.add_grade(10)
    student.add_grade(6)
    student.add_grade(1000)
    student.display_info()
