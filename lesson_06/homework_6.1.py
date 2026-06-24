# ДЗ 6.1. Рахування унікальних символів в строці
# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

text = input("Enter text: ")
MAX_UNIQUE_SYMBOLS = 10

if len(set(text)) > MAX_UNIQUE_SYMBOLS:
    print(True)
else:
    print(False)