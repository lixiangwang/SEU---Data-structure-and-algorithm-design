# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""

def find_symmetry(s):
    k = len(s)
    olist = [0] * k  
    nList = [0] * k  
    logestSubStr = ""
    logestLen = 0
 
    for j in range(0, k):
        for i in range(0, j + 1):
            if j - i <= 1:
                if s[i] == s[j]:
                    nList[i] = 1                    
                    len_t = j - i + 1
                    if logestLen < len_t:               
                        logestSubStr = s[i:j + 1]
                        logestLen = len_t
            else:
                if s[i] == s[j] and olist[i+1]:    
                    nList[i] = 1                    
                    len_t = j - i + 1
                    if logestLen < len_t:
                        logestSubStr = s[i:j + 1]
                        logestLen = len_t
        olist = nList                            
        nList = [0] * k                          
    return logestSubStr ,len(logestSubStr)


s=[1, 2, 3, 4, 3, 1]
s2=[1, 2, 3, 4, 4, 3, 1] 
substr,length=find_symmetry(s2)
print('最长对称子序列：',substr)
print('最长对称子序列长度:',length)