import multiprocessing as mp
import time


"""Рекурсивный алгоритм"""

def catalan_recursive(n):
    if n == 0:
        return 1
    else:
        catalan = 0
        for i in range(n):
            catalan += catalan_recursive(i) * catalan_recursive(n - i - 1)
        return catalan


"""Динамический алгоритм"""

def catalan_dynamic(n):
    catalan = [0] * (n + 1)
    catalan[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]
    return catalan[n]


def test_multiprocessing(func_1, func_2, inputs):
    start = time.time()

    with mp.Pool(processes=4) as pool:
        outputs_1 = pool.map(func_1, inputs)

    with mp.Pool(processes=4) as pool:
        outputs_2 = pool.map(func_2, inputs)

    end = time.time()
    
    print(outputs_1, outputs_2)
    print(end - start)

def recursive_mp():
    start = time.time()

    with mp.Pool(processes=4) as pool:
        outputs_1 = pool.map(catalan_recursive, [1, 2, 3, 4])

    with mp.Pool(processes=4) as pool:
        outputs_2 = pool.map(catalan_recursive, [5, 6, 7, 8])
    
    with mp.Pool(processes=4) as pool:
        outputs_3 = pool.map(catalan_recursive, [9, 10, 11, 12])
    
    with mp.Pool(processes=4) as pool:
        outputs_4 = pool.map(catalan_recursive, [13, 14, 15, 16])
    
    additional = mp.Process(target=catalan_recursive, args=17)

    additional.start()
    additional.join()

    end = time.time()
    
    print(outputs_1 + outputs_2 + outputs_3 + outputs_4)
    print(end - start)

if __name__ == '__main__':
    recursive_mp()

# x = np.r_[1:(17 + 1):1]
# graphics(catalan_recursive, catalan_dynamic, x)