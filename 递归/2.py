# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""

def solve(list_a):
    for i in range(len(list_a)):
        if type(list_a[i])==list:
            list_a[i] = solve(list_a[i])
            continue
    list_a = list_a[::-1]
    return list_a

if __name__ == '__main__':
    list_a = [1, [2, 3], 4, [5, [6, 7], 8], 9]
    print(solve(list_a))