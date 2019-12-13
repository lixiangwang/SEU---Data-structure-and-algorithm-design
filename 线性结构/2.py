# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""

def find_middle(array):
    
    length=len(array)
    rightMin = [None]*length
    rightMin[length - 1] = array[length - 1]
    
    for i in range(length-2,-1,-1):
        rightMin[i] = min(rightMin[i + 1], array[i])
        
    left_max=0
    for i in range(length):
    
        left_max=max(left_max,array[i])
        
        if left_max == rightMin[i]:
            print('Have the x:',array[i])
    
        
        
             
a=[3, 1, 6, 4, 5, 7, 9, 8, 10, 14, 12 ]
find_middle(a)