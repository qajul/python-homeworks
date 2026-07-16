def calculate_sum(numbers_string):
    try:
        numbers = numbers_string.split(",")
        total = 0

        for number in numbers:
            total = total + int(number)

        return total

    except ValueError:
        return "Не можу це зробити!"


my_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for item in my_list:
    print(calculate_sum(item))