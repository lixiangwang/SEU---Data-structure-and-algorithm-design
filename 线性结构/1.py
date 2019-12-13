# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""


def find_x_1_3(array):
    count_m=0
    count_n=0
    m=n=array[0]
    
    for i in array:
        if i == m:  
            count_m+=1
            continue
        if i == n:
            count_n+=1
            continue
        if count_m == 0:
            m = i
            count_m+=1
            continue
        if count_n ==0:
            n = i
            count_n+=1
            continue
            
        count_m-=1
        count_n-=1
    
    count_m=0
    count_n=0
    
    for i in array:
        if i==m:
            count_m+=1
        elif i==n:
            count_n+=1
            
    if count_m>len(array)/3:
        print('Have the x:',m)
    if count_n>len(array)/3:
        print('Have the x:',n)
        
        
a=[1,1,1,1,1,1,1,1,3,3,4,2,2,5,2,2,2,2,2,5,2]
find_x_1_3(a)