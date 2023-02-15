#!/usr/bin/env python3

"""
Реализация алгоритма Рабина-Карпа с модульными тестами
"""

import unittest

def rabin_karp(text, pattern):
    """
    Поиск всех вхождений алгоритмом Рабина-Карпа

    Параметры:
    ----------
        text: str
            текст
        pattern: str
            образец

    Возвращаемое значение
    ---------------------
        список позиций в тексте, с которых начинаются вхождения образца
    """
    result = []
    # Менять отсюда =) ---- vvvvv ----

    b = 10 # Константа из формулы скользящего хеша
    q = 256 # Модульная константа из формулы скользящего хеша

    n = len(text)
    m = len(pattern)

    if text == '': # Проверка вырожденного случая для текста
        return []
    if pattern == '': # Проверка вырожденного случая для шаблона
        return [i for i in range(n)]

    multiplier = pow(b, m - 1) % q # Максимальная тепень константы b из формулы скользящего хеша
	
    t, p = 0, 0
    for i in range(m):
        t = (b * t + ord(text[i])) % q # Вычисление хеша для текста
        p = (b * p + ord(pattern[i])) % q # Вычисление хеша для шаблона

    for i in range(n - m + 1):
        if p == t and text[i: i + m] == pattern:
            result.append(i) # Вхождение образца найдено
        if i < n - m:
            t = (b * (t - ord(text[i]) * multiplier) + ord(text[i + m])) % q # Вычисление хеша для следующей "ячейки" текста
            if t < 0:
                t = t + q # Избавляемся от отрицательных значений

    # Менять до сюда =) ---- ^^^^^ ----
    return result


class RabinKarpTest(unittest.TestCase):
    """Тесты для метода Рабина-Карпа"""

    def setUp(self):
        """Инициализация"""
        self.text1 = 'axaxaxax'
        self.pattern1 = 'xax'
        self.text2 = 'bababab'
        self.pattern2 = 'bab'

    def test_return_type(self):
        """Проверка того, что функция возвращает список"""
        self.assertIsInstance(
            rabin_karp(self.text1, "x"), list,
            msg="Функция должна возвращать список"
        )

    def test_returns_empty(self):
        """Проверка того, что функция, когда следует, возвращает пустой список"""
        self.assertEqual(
            [], rabin_karp(self.text1, "z"),
            msg="Функция должна возвращать пустой список, если нет вхождений"
        )
        self.assertEqual(
            [], rabin_karp("", self.pattern1),
            msg="Функция должна возвращать пустой список, если текст пустой"
        )
        self.assertEqual(
            [], rabin_karp("", ""),
            msg="Функция должна возвращать пустой список, если текст пустой, даже если образец пустой"
        )

    def test_finds(self):
        """Проверка того, что функция ищет все вхождения непустых образцов"""
        self.assertEqual(
            [1, 3, 5], rabin_karp(self.text1, self.pattern1),
            msg="Функция должна искать все вхождения"
        )
        self.assertEqual(
            [0, 2, 4], rabin_karp(self.text2, self.pattern2),
            msg="Функция должна искать все вхождения"
        )

    def test_finds_all_empties(self):
        """Проверка того, что функция ищет все вхождения пустого образца"""
        self.assertEqual(
            list(range(len(self.text1))), rabin_karp(self.text1, ""),
            msg="Пустая строка должна находиться везде"
        )

# Должно выдать:
# --------------
# Ran ... tests in ...s
# OK

# Запуск тестов
if __name__ == '__main__':
    unittest.main()
