# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier

        if result > 25:
            break

        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1

multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_function(a, b):
    return a + b

result = sum_function(1, 3)
print(result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Середнє арифметичне: {average(numbers)}")

# task 4 """ Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
def reverse_string(text):
    return text[::-1]

text = "Hello World"
print(f"Рядок у зворотному порядку: {reverse_string(text)}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    return max(words, key=len)

result = longest_word(["cucumber", "tomato", "onion", "garlic"])
print(f"Найдовше слово {result}")


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):

    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7-10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
def create_string_list(lst1):
    """ Домашка 6.3 - Повертає новий список, який містить лише рядки з переданого списку"""
    lst2 = []
    for item in lst1:
        if isinstance(item, str):
            lst2.append(item)
    return lst2

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

result = create_string_list(lst1)

print(result)


# task 8

list_value = list(range(10))

def sum_even_numbers(list_value):
    """ Домашка 6.4 - рахує сумму усіх ПАРНИХ чисел в заданому лісті"""
even_sum = 0
for number in list_value:
    if number % 2 == 0:
        even_sum += number

print("Sum of even numbers:", even_sum)

# task 9
def total_area(black_sea_area, azov_sea_area):
    """ Домашка 3.4 - рахує суму площ морів"""
    total_area = black_sea_area + azov_sea_area
    return total_area

black_sea_area = 436_402
azov_sea_area = 37_800

result = total_area(black_sea_area, azov_sea_area)

print(f"Разом Чорне та Азовське моря займають {result} км².")

# task 10
def find_computer_price(payment, time):
    """Домашка 3.6 - Повертає повну вартість комп'ютера за щомісячним платежем та кількістю місяців."""
    computer_price = payment * time
    return computer_price
payment = 1179
time = 18

result = find_computer_price(payment, time)
print(f"{result} грн. становить вартість комп'ютера")