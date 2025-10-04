import unittest


def guess_number(target: int, numbers: list[int], method: str = "linear" ) -> list:
    """
    Угадывает загаданное число с помощью выбранного алгоритма.
        Метод угадывания:
        - "linear" — медленный перебор (инкремент по одному);
        - "binary" — бинарный поиск.
        По умолчанию используется "linear".
    """
    sorted_numbers = sorted(numbers)

    attempts = 0

    if method == "linear":
        for num in sorted_numbers:
            attempts += 1
            if num == target:
                return num, attempts

    elif method == "binary":
        left, right = 0, len(sorted_numbers) - 1
        while left <= right:
            attempts += 1
            mid = (left + right) // 2
            if sorted_numbers[mid] == target:
                return sorted_numbers[mid], attempts
            elif sorted_numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

    else:
        print('Неправильный тип поиска')

    return -1, attempts


def get_user_input() -> list:
    """ Вспомогательная функция для ввода данных с клавиатуры. """
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    target = int(input("Введите число, которое нужно угадать: "))
    method = input("Введите метод угадывания (linear/binary): ").strip().lower()

    numbers = list(range(start, end + 1))
    return target, numbers, method


class TestMath(unittest.TestCase):
    def test_bin_positive(self):
        self.assertEqual(guess_number(1, [1,2,3], 'binary'), (1, 2))

    def test_bin_negative(self):
        self.assertEqual(guess_number(-4, [-6,-5,-4,-3,-2], 'binary'), (-4, 1))

    def test_bin_none(self):
        self.assertEqual(guess_number(1, [2,3,4], 'binary'), (-1, 2))

    def test_lin_positive(self):
        self.assertEqual(guess_number(1, [1,2,3]), (1, 1))

    def test_lin_negative(self):
        self.assertEqual(guess_number(-4, [-6,-5,-4,-3,-2]), (-4, 3))

    def test_lin_none(self):
        self.assertEqual(guess_number(1, [2,3,4], 'linear'), (-1, 3))

unittest.main(argv=[''], verbosity=2, exit=False)
