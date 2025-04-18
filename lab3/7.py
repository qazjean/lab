class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
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
        print(f"{self.name} ведет {self.subject} у следующих студентов:")
        for s in self.students:
            s.display_info()

#Новый фрагмент кода отсюда!!
class Assistant(Teacher, Student):
    def __init__(self, name, age, student_id, subject):
        #извините, честно говоря, я не совсем поняла, как сделать наследование иначе
        #я пыталась  Student.__init__(self, name, age, student_id), а потом Teacher.__init__(self, name, age, subject)
        #я понимаю, почему это не сработало, но обойти это смогла только так (зато так точно работает)
        Person.__init__(self, name, age) #наследование от персон, а дальше атрибуты учителя,ученика
        self.student_id = student_id
        self.grades = []
        self.subject = subject
        self.students = set()

    def help_student(self, student: Student):
        print(f"Ассистент {self.name} помогает студенту {student.name} с предметом {self.subject}")

if __name__ == "__main__":  # пример
    teach = Teacher("Прощаев Александр Аркадьевич", 30, "Базы данных")
    student = Student("Лизочка Пронина", 18, 1)
    teach.add_student(student)
    student2 = Student("Алиса Летуновская", 18, 2)
    teach.add_student(student2)

    # Создаем ассистента (он одновременно и студент, и учитель)
    assistant = Assistant("Мария Учаева", 19, 3, "обж")

    assistant.add_student(student)
    assistant.add_student(student2)     # Добавляю студентов ассистенту (метод учителя)

    assistant.help_student(student)
    assistant.help_student(student2)# Ассистент помогает студенту (метод ассистента)

    print("\nСписок студентов ассистента:")
    assistant.list_students()  # Метод из Teacher

    teach.add_student(assistant)   #как у студента, у ассистента тоже есть преподаватель
    #проверим это, вызвыв:
    teach.list_students()
