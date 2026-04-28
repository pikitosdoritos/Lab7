# 1. Напишіть набір функцій, які виконують наступні завдання:

# 1) Функція приймає іменовані аргументи width та height (ширина і висота прямокутника) і обчислює його площу.
# 2) Функція приймає іменовані аргументи name (ім’я) та age (вік) користувача і повертає рядок з вітанням.
# 3) Функція приймає два числа і повертає їх добуток. При цьому один аргумент має бути позиційним, а другий — іменованим.
# 4) Функція обчислює середнє арифметичне чисел у списку, переданому як позиційний аргумент.
# 5) Функція додає два числа, передані як позиційні аргументи.
# 6) Функція приймає іменований аргумент divider та список чисел numbers і повертає список тих чисел, які діляться на divider без остачі.

print("==" * 80)
print("Завдання 1")

# 1)
def rectangle_area(*, width, height):
    s = width * height
    return s

# 2)
def greeting(*, name, age):
    return f"Hello, {name}. You are {age} years old."

# 3)
def multiply(a, *, b):
    return a * b

# 4)
def average(*numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)

# 5)
def add(x, y):
    return x + y

# 6)
def divide(*, divider, numbers):
    return [num for num in numbers if num % divider == 0]

# ТЕСТУВАННЯ ФУНКЦІЙ

print("1) Площа прямокутника:")
print(rectangle_area(width=5, height=10))  

print("\n2) Вітання:")
print(greeting(name="Nikita", age=19))

print("\n3) Добуток (позиційний + іменований):")
print(multiply(4, b=6))  

print("\n4) Середнє арифметичне:")
print(average(1, 2, 3, 4, 5)) 

print("\n5) Сума двох чисел:")
print(add(7, 8))  

print("\n6) Числа, що діляться на divider:")
print(divide(divider=3, numbers=[1, 3, 6, 7, 9, 10]))  


# 2. Напишіть набір функцій, які виконують наступні завдання:

# 1) Функція приймає словник і друкує його ключі та значення.
# 2) Функція приймає словник і повертає список ключів, впорядкованих за їхніми значеннями в порядку зростання.
# 3) Функція приймає змінну кількість позиційних числових аргументів і повертає їх суму.
# 4) Функція приймає список чисел і повертає їх суму. Функція повинна мати змінну кількість іменованих аргументів.
# 5) Функція приймає список чисел і повертає їх середнє значення. Функція повинна мати змінну кількість позиційних аргументів.

print("==" * 80)
print("Завдання 2")

# 1)
def print_dict(d):
    for key, value in d.items():
        print(f"{key}: {value}")
        
# 2)
def sort_dict(d):
    return [key for key, value in sorted(d.items(), key=lambda item: item[1])]

# 3)
def sum_args(*args):
    return sum(args)

# 4)
def sum_kwargs(list_of_numbers, **kwargs):
    return sum(item for item in list_of_numbers)

# 5)
def average_args(*args):
    return sum(args) / len(args) if args else 0