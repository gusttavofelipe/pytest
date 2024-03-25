import random


def divide(num1, num2):
    return num1 / num2 if num1 != 0 else None


def multiply_numbers(a: int | float, b: int | float) -> float:
    return a * b


def length(list_):
    return len(list_)


def sum_numbers(a: int | float, b: int | float) -> float:
    return a + b


def double_and_sum(number_list) -> int:
    return sum(x * 2 for x in number_list)


def classify_age(age):
    if age < 18:
        return "teen"
    elif age < 50:
        return "adult"
    else:
        return "senior"


def calc_total_price(price, discount_percent, tax_percent) -> float:
    return round(price * (1 - discount_percent / 100) * (1 + tax_percent / 100), 2)


def calc_fatorial(number: int):
    if number == 0:
        return 1
    elif number < 0:
        raise ValueError("Number must be positive")
    return number * calc_fatorial(number - 1)


def generate_random_number_list(positive=True) -> list[int]:
    min_value = 0 if positive else -1001
    max_value = 1001 if positive else 0

    return [random.randint(min_value, max_value) for _ in range(random.randint(0, 100))]


def access_index(index: int):
    try:
        list_ = [1, 2, 3]
        return list_[index]

    except IndexError:
        raise IndexError("Index out of range")
    except TypeError:
        raise TypeError("Invalid input")
