# Натуральный логарифм (ряд Тейлора)

import math

x = float(input("\n|x| < 1, x = "))
n = int(input("Кол-во слагаемых (точность вычислений): "))

def my_ln(x):
    s = 0
    for i in range(n + 1):
        s += (((-1) ** i) * (x ** (i + 1))) / (i + 1)
    return s

print("\nln(1 + " + str(x) + ") = ", end = '')
print(str(math.log(1 + x)) + " (библиотечная ф-ия)" )
print("              " + str(my_ln(x)) + " (cамодельная ф-ия)")
