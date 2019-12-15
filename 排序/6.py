# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""

def disassemble(a,b):           #a分子，b分母
    c = 0
    temp = ''
    while (a >= 1):
        if b % (a - 1) == 0:
            temp = '1/' + str(b // (a - 1)) + '+' + '1/' + str(b)
            print(temp)
            break
        else:
            c = (b // a) + 1
            temp = '1/' + str(c) + '+'
            print(temp, end="")
            a = a * c - b
            b = b * c
            if b % a == 0:
                b = b // a
                a = 1
                temp = str(a) + '/' + str(b)
                print(temp)
                break



if __name__ == '__main__':
    disassemble(5, 8)
    disassemble(7, 8)
    disassemble(9, 10)
    disassemble(10, 11)


