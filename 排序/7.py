# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""

def min_add(s):
    n = len(s)
    db = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                db[i][j] = 0
            elif s[i] == s[j]:
                db[i][j] = db[i + 1][j - 1]
            else:
                db[i][j] = min(db[i + 1][j], db[i][j - 1]) + 1
    return db[0][-1]


if __name__ == '__main__':
    list =[1,2,3,2,5]
    list_new = [str(x) for x in list]
    string = ''.join(list_new)
    result=min_add(string)
    print('至少需要插入%d个元素'%result)
