#Завдання 1
#Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer, які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
#Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.
#Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department


class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )
        self.team_size = team_size


def test_teamlead():
    team_lead = TeamLead(
        "Yuliia",
        3000,
        "QA",
        "Python",
        4
    )

    assert team_lead.name == "Yuliia"
    assert team_lead.salary == 3000
    assert team_lead.department == "QA"
    assert team_lead.programming_language == "Python"
    assert team_lead.team_size == 4