# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""
import numpy as np

def quick_sort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':

    arr = np.mat([[22,44,87,50,18,42],[21,96,25,47,42,21],[17,42,46,54,78,29],[52,43,89,42,27,39]])
    list0 = [22,44,87,50,18,42,21,96,25,47,42,21,17,42,46,54,78,29,52,43,89,42,27,39]
    print('处理前的矩阵为：\n', arr)

    list_sort = quick_sort(list0)
    arr1 = np.mat(list_sort).reshape(arr.shape[0], arr.shape[1])

    print('处理后的矩阵为：\n', arr1)