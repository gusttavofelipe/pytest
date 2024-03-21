def email_is_valid(email):
    return "@" in email and "." in email


def divide(num1, num2):
    return num1 / num2 if num1 != 0 else None


def is_positive(number):
    return number > 0


def length(list_):
    return len(list_)


def sum_numbers(a, b):
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
