#Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def get_generator(n):
    return (x for x in range(n + 1) if x % 2 == 0)

#Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

#Реалізуйте ітератор для зворотного виведення елементів списку.
class ReverseIterator:
    def __init__(self, data_list):
        self.data_list = data_list
        self.index = len(data_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        element = self.data_list[self.index]
        self.index -= 1
        return element

#Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class Iterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        current_number = self.current
        self.current += 2

        return current_number

#Напишіть декоратор, який логує аргументи та результати викликаної функції.
def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Функція '{func.__name__}'")
        print(f"Аргументи: args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"Функція '{func.__name__}' повернула: {result}")
        return result

    return wrapper

#Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def catch_errors(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
            return result
        except Exception as error:
            print(f"Виникла помилка: {error}")
            return None

    return wrapper

