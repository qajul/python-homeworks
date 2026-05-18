# task 01
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, '
    '"if you only walk long enough."'
)

# task 02
for symbol in alice_in_wonderland:
    if symbol == "'":
        print(symbol)

# task 03
print(alice_in_wonderland)

# task 04
black_sea_area = 436_402
azov_sea_area = 37_800
total_area = black_sea_area + azov_sea_area
print(f"Разом Чорне та Азовське моря займають {total_area} км².")

# task 05
total_products = 375_291
first_and_second_storage = 250_449
second_and_third_storage = 222_950

# Кількість товарів на першому складі
first_storage = total_products - second_and_third_storage
# Кількість товарів на третьому складі
third_storage = total_products - first_and_second_storage
# Кількість товарів на другому складі
second_storage = total_products - first_storage - third_storage

print(f"На першому складі: {first_storage} товарів.")
print(f"На другому складі: {second_storage} товарів.")
print(f"На третьому складі: {third_storage} товарів.")

# task 06
payment = 1179
time = 18
computer_price = payment * time
print(f"{computer_price} грн. становить вартість комп'ютера")

# task 07
print(f"8019 : 8 = остача {8019 % 8}")
print(f"9907 : 9 = остача {9907 % 9}")
print(f"2789 : 5 = остача {2789 % 5}")
print(f"7248 : 6 = остача {7248 % 6}")
print(f"7128 : 5 = остача {7128 % 5}")
print(f"19224 : 9 = остача {19224 % 9}")

# task 08
pizza_big = 4 * 274
pizza_medium = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21

price = (pizza_big + pizza_medium + juice + cake + water)
print(f"{price} грошей знадобиться для даного замовлення.")

# task 09
photos = 232
photos_can_be_on_page = 8

pages = photos // photos_can_be_on_page
print(f"{pages} сторінок знадобиться Ігорю, щоб вклеїти всі фото.")


# task 10
distance = 1600
fuel_100_km = 9
V = 48
fuel_needed = (distance / 100) * fuel_100_km
refuelling = fuel_needed // V
print(f"Для подорожі знадобиться {fuel_needed} літрів бензину.")
print(f"Родині необхідно щонайменше {refuelling} рази заїхати на заправку.")