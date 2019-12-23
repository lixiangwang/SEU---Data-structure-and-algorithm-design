# encoding: utf-8

def solution(i, n):
    a = (i + 2) * 2
    print("经过第%d个村子"%(n-1))
    print("有%d只鸭子\n"%a)
    n = n- 1
    if n> 0:
        solution(a,n)

if __name__ == '__main__':
    solution(2,3)