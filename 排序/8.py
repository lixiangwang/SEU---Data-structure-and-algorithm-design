# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""


def integerBreak(num):
    result_multi = 1
    result_list = []
    if num<=1:
        result_multi = 1
        result_list.append(1)
    else:
        if num % 3 == 0:
            result_multi = 3**(num//3)
            for i in range(num//3):
                result_list.append(3)

        if num % 3 ==1 and num>1:
            for i in range(num//3-1):
                result_list.append(3)
            result_list.append(2)
            result_list.append(2)
            for m in result_list:
                result_multi *=m

        if num %3 ==2:
            for i in range(num//3):
                result_list.append(3)
            result_list.append(2)
            for m in result_list:
                result_multi *=m

    return result_list,result_multi

if __name__ == '__main__':
    result_list, result_multi = integerBreak(8)
    print(result_list)
    print(result_multi)