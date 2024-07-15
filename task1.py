def caching_fibonacci():
    """Кешування чисел Фібоначчі у словник.

        Параметри:
        -

        Повертає:
        Callable[[int], int]: Функція fibonacci(n: int]) -> int
    """

    cache = {}

    def fibonacci(n=1):
        """Обчислення числа Фібоначчі з рекурсією та кешуванням результатів для ефективного підрахунку.

            Параметри:
                n (int): номер числа Фібоначчі (1 за замовчуванням)

            Повертає:
                int: Значення числа Фібоначчі

        """

        nonlocal cache

        if n <= 1:
            return n
        # Додавання числа в кеш, якщо досі там не існує
        if n not in cache:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)

        return cache[n]

    return fibonacci


fibonacci_cache = caching_fibonacci()

for i in range(10):
    print(f'Fibonacci({i}) = {fibonacci_cache(i)}')
