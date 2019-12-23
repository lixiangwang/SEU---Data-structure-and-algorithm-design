# encoding: utf-8

import numpy as np

def find_path(array):
    m = 1
    n = 4
    med = np.zeros(shape=(4, 4))
    while m:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    med[i][j] += array[i][k] * array[k][j]

        for i in range(n):
            for j in range(n):
                array[i][j] = med[i][j]
        m -= 1

    num = 0
    for i in range(n):
        for j in range(n):
            num += array[i][j]
    print(num)


if __name__ == '__main__':
    matrix = [[0, 1, 0, 1],  # 0
              [0, 0, 1, 1],  # 1
              [1, 1, 0, 1],  # 2
              [0, 0, 1, 0]]  # 3
    print(find_path(matrix))