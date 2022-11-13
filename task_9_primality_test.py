import random


def is_prime(x): 
    """Наивная проверка на простоту"""
    b = True
    for i in range(2, int(x ** 0.5) + 2):
        if x % i == 0:
            b = False
            break
    return b


def gcd(a, b):
    """Алгоритм Евклида для работы алгоритма Соловея-Штрассена"""
    if a >= b:
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    else:
        a, b = b, a
        return gcd(a, b)


def solovey_shtrassen(n, k):
    """Тест на простоту Соловея-Штрассена"""
    for i in range(1, k + 1):
        a = random.randint(2, n - 1)
        if gcd(a, n) > 1:
            return False
        try:                                           # Питон работает медленно, и на больших числах
            ((a ** ((n - 1) / 2)) - (a / n)) % n == 0  # может возникнуть ошибка OverflowError, которая
        except OverflowError:                          # останавливает программу, но не означает некорректную
            return False                               # работу алгоритма. Поэтому я её обхожу =)
    return True


def print_s_s(n, k):
    """Печать solovey_shtrassen"""
    if solovey_shtrassen(n ,k):
        print(str(n) +  " - простое число с вероятностью " + str(1 - (2 ** (-k))) + ". Проверим наивным алгоритмом: " + str(is_prime(n)))
    else:
        print(str(n) +  " - составное число")


"""Проверка работы программы"""

print("--------------------------------------------------------------------------------")
print("Чем больше k (второй аргумент), тем точнее вычисления.")
print("Также роль в точности и скорости вычислений играет случайный выбор переменной a.")
print("Запустите программу несколько раз, чтобы убедиться в этом.\n")
print_s_s(20, 1)
print_s_s(20, 2)
print('')
print_s_s(17, 1)
print_s_s(17, 2)
print_s_s(17, 3)
print_s_s(17, 20)
print('')
print_s_s(62745, 1)
print_s_s(23456789877, 1)
print("--------------------------------------------------------------------------------")
