class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person): #не совсем поняла задание, но, как я поняла, ввести класс студент все же нужно,
    #тк в атрибутах класса учитель есть список объектов студент.
    #Так что я скопировала фрагмент кода из прошлого задания, но так же добавила наследование от класса персон
    #тк ученики тоже люди
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            print(f"oh! оценки {grade} нет")

    def get_average(self):
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        return 0.0

    def display_info(self): #выведет информацию о студентах
        print(f"Имя студента: {self.name}")
        print(f"id студента: {self.student_id}")
        print(f"Его средний балл: {self.get_average()}")
        print(f"Оценки: {', '.join(map(str, self.grades))}")
        print()

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.students = set()
    def add_student(self, student: Student):
        self.students.add(student)

    def remove_student(self, student: Student):
        try:
            self.students.remove(student)
        except KeyError: #на всякий случай (нельзя удалить студента, которого и так не было)
            print(f"Студент {student.name} не найден в списке")
    def list_students(self):
        print(f"Учитель {self.name} ведет {self.subject} у следующих студентов:")
        for s in self.students:
            s.display_info() #для объекта студент используем метод класса студент
            
#пример
if __name__ == "__main__":  # пример
    teach = Teacher("Прощаев Александр Аркадьевич", 35, "Базы данных")
    student = Student("Лизочка Пронина", 18, 100)
    teach.add_student(student)
    teach.list_students()
