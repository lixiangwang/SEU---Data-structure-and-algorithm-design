# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""


def Combinations(L, k):
    """List all combinations: choose k elements from list L"""
    n = len(L)
    result = []  # To Place Combination result
    for i in range(n - k + 1):
        if k > 1:
            newL = L[i + 1:]
            Comb, _ = Combinations(newL, k - 1)
            for item in Comb:
                item.insert(0, L[i])
                result.append(item)
        else:
            result.append([L[i]])
    return result, len(result)


def solve(L, res):
    for k in range(len(res)):
        res.append(res[k][::-1])
    for i in L:
        res.append([i, i])
    return res


if __name__ == '__main__':
    L = [1, 2, 3]
    res, length = Combinations(L, 2)
    result = solve(L, res)
    print('所有的可重复排列为：', result)