# ДЗ 6.4. Сумуємо числа
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

list_value = list(range(10))

even_sum = 0

for number in list_value:
    if number % 2 == 0:
        even_sum += number

print("Sum of even numbers:", even_sum)