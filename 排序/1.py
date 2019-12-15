# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""
def left_odd(array):
    divP = 0
    for i in range(len(array)):
        if array[i] % 2 == 1:
            searchP = i
            while searchP > divP:
                array[searchP], array[searchP - 1] = array[searchP - 1], array[searchP]
                searchP -= 1
            divP += 1
    return array

if __name__ == '__main__':
    list = [3, 2, 6, 1, 4, 9, 8, 5, 11, 7]
    print('处理前的序列为：', list)
    list2 = left_odd(list)
    print('处理后的序列为：',list2)

