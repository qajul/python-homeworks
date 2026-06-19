class Student:

    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_grade):
        print(f"Середній бал змінено з {self.average_grade} на {new_grade}")
        self.average_grade = new_grade


student1 = Student("Юлія", "Децик", 25, 91)

print(f"Ім'я: {student1.name}\n"
      f"Прізвище: {student1.surname}\n"
      f"Вік: {student1.age}\n"
      f"Середній бал: {student1.average_grade}")

student1.change_average_grade(99)

print(f"Оновлений середній бал: {student1.average_grade}")