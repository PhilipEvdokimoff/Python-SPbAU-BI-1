#!/usr/bin/env python3

"""
Натуральный логарифм (ряд Тейлора):
сравнение библиотечной и "самодельной" функций
"""

import math

x = float(input("\n|x| < 1, x = "))
iterations = int(input("Кол-во слагаемых (точность вычислений): "))

def my_ln(x):
    """
    Вычисление натурального логарифма при помощи частичного суммирования ряда Тейлора
    """
    partial_sum = 0
    for i in range(iterations + 1):
        partial_sum += (((-1) ** i) * (x ** (i + 1))) / (i + 1) # Cама формула частичной суммы
    return partial_sum

print("\nln(1 + " + str(x) + ") = ", end = '')
print(str(math.log(1 + x)) + " (библиотечная ф-ия)" )
print("              " + str(my_ln(x)) + " (самодельная ф-ия)")

"""
Построение графиков "нашего" и библиотечного логарифмов
"""

from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'svg')

import matplotlib.pyplot as plt
import numpy as np

v_ln = np.vectorize(my_ln)
print(my_ln, v_ln)

x = np.r_[-0.999:0.999:0.001] # Представление интервала (-1, 1)

plt.plot(x, np.log(1 + x), label = 'библиотечный $\ln (x)$')
plt.plot(x, v_ln(x), label = 'самодельный $\ln (x)$')
plt.xlabel('Ось абсцисс')
plt.ylabel('Ось ординат')
plt.title('Натуральный логарифм, $|x| < 1$')
plt.legend()
plt.show()