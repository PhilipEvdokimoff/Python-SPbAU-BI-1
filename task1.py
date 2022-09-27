import math # Импорт пакета math (математика)
import numpy # Импорт пакета numpy (математика и большие массивы)
import matplotlib.pyplot as mpp # Импорт пакета matplotlib (графики)

# Эта программа рисует график функции, заданной выражением ниже

if __name__ == '__main__': # Добавление "логики" в код
    arguments = numpy.arange(0, 200, 0.1) # Возвращает одномерный массив с равномерно разнесенными значениями внутри заданного интервала
    mpp.plot(arguments, [math.cos(a) * math.cos(a/20.0) for a in arguments]) # plot() строит график по тригоном. ф-ям
    mpp.show()# Показывает график