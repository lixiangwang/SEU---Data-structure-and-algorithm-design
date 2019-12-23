# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if(not candidates):
            return []
        n=len(candidates)
        candidates.sort()
        res=[]
        def helper(i,tmp,target):
            if(target==0):
                res.append(tmp)
                return
            if(i==n or target<candidates[i]):
                return
            for j in range(i,n):
                if(j>i and candidates[j]==candidates[j-1]):
                    continue
                helper(j+1,tmp+[candidates[j]],target-candidates[j])
        helper(0,[],target)
        return res

if __name__ == '__main__':
    solution = Solution()
    List = [4, 5, 7, 3, 9, 6, 2 ]
    target = 15
    result = solution.combinationSum2(List,target)
    print('所有的子集为:',result)