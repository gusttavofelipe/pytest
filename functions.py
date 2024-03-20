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
