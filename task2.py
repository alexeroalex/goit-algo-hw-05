from typing import Callable
import re


def generator_numbers(text: str):
    """Генератор дійсних чисел, знайдених в обраному тексті.

    Параметри:
        text (str): Рядок для пошуку чисел

    Повертає:
        str: Наступне число знайдене в тексті.

    """

    numbers = re.findall(r'\d+\.\d+|\d+', text)

    for i in numbers:
        yield i


def sum_profit(text: str, generator: Callable):
    total_sum = 0

    # Сумування чисел з тексту
    for num in generator(text):
        total_sum += float(num)

    return total_sum


sentence = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, "
            "доповнений додатковими надходженнями 27.45 і 324.00 доларів.")
total_income = sum_profit(sentence, generator_numbers)
print(f"Загальний дохід: {total_income}")