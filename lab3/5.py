class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            print(f"oh! оценки {grade} нет")
    def get_average(self):
        if len(self.grades) > 0:
            return sum(self.grades)/len(self.grades)
        return 0.0
    def display_info(self): #красиво (на мой взгляд) вывожу информацию о студентах
        print(f"Имя студента: {self.name}")
        print(f"id студента: {self.student_id}")
        print(f"Его/её средний балл: {self.get_average()}")
        print(f"Оценки: {', '.join(map(str, self.grades))}")

    def __str__(self):
        return (f"Студент: {self.name}, ID: {self.student_id}, "
                f"оценок: {len(self.grades)}, средний балл: {self.get_average():.1f}")

    def __eq__(self, other):
        if isinstance(other, Student):  #проверяет принадлежность объекта к классу
            return self.student_id == other.student_id
        return False

    def __len__(self):
        return len(self.grades) #возвращает длину списка (количество оценок)
      
if __name__ == "__main__": #пример
    student = Student("Лизочка Пронина", "1511")
    student.add_grade(10)
    student.add_grade(6)
    student.add_grade(1000)
    student.display_info()

    student2 = Student("Полина Лубенец", "1511")  # Такой же ID
    print(student)  # Автоматически вызовет __str__ (текстовое представление объекта)
    print(student == student2)  # сравнение по ID благодаря магическому методу (результат - true)
    print(f"Количество оценок у student1: {len(student)}")  #определит количество оценок так, как если бы класс student был встроенным типом данных
