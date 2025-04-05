class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            raise ValueError("oh! Такой оценки нет")
    def get_average(self):
        if len(self.grades) > 0:
            return sum(self.grades)/len(self.grades)
        return 0.0
    def display_info(self):
        print(f"Имя студента: {self.name}")
        print(f"id студента: {self.student_id}")
        print(f"Его средний балл: {self.get_average()}")
        print(f"Его оценки: {", ".join(map(str, self.grades))}")

student = Student("Лизочка Пронина", "1511")
student.add_grade(10)
student.add_grade(5)
student.display_info()
