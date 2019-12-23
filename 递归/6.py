# encoding: utf-8

from typing import List
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        n = len(A)
        total = sum(A)
        if total % 3 != 0:
            return False

        p = total // 3
        tmp, t = 0, 0
        for i in range(n):
            tmp += A[i]
            if tmp == p:
                t = i
                break
        tmp = 0
        for j in range(t + 1, n):
            tmp += A[j]
            if tmp == p:
                return sum(A[j + 1:]) == p
        return False
