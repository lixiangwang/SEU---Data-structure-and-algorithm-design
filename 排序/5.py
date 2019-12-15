# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""

class Solution:
    def removeK(self, num, k):
        if k >= len(num):
            return "0"
        i = 0
        while i < len(num) - 1 and k > 0:
            if int(num[i])>int(num[i+1]):
                num=num[0:i]+num[i+1:]
                if i>0:
                    i-=1
                k-=1
            else:i+=1
        num=num[:len(num)-k]             
        return str(int(num))



if __name__ == '__main__':
    list0 = '1432219'
    solution = Solution()
    min_num = solution.removeK(list0, 3)
    print('最小数为：\n', min_num)



