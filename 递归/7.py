# encoding: utf-8


A = [None for i in range(0, 10)]
result_list = []
def is_prime(n):
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True

def dfs(cur):
    if cur == N:
        if is_prime(A[0]+A[N-1]):
            result_list.append(A[:N])
    else:
        for i in range(1, N+1):
            if i not in A[:cur]:
                if cur == 0 or is_prime(i+A[cur-1]):
                    A[cur] = i
                    dfs(cur+1)
    return result_list

N = 10
result_list = dfs(0)
print('符合题意的一个条件为:',result_list[0])