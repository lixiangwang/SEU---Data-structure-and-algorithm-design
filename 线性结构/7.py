# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""

import numpy as np

# def find_max(arr):
#     if arr is None or len(arr) == 0:
#         return 0   
    
#     head = tail =0
#     ap=[]
#     flag=0
#     max_sum = cur_sum = float('-inf')
#     for i in range(len(arr)):
#         if cur_sum <= 0:
#             cur_sum = arr[i]
#         else:
#             flag+=1
#             if flag ==1:
#                 head=i-1
#             cur_sum += arr[i]
            
#         if cur_sum > max_sum:
#             tail = i
#             max_sum = cur_sum
            
#     for i in range(tail-head+1):
#         ap.append(arr[head+i])
        
#     return max_sum ,ap

def find_max(arr):
    if arr is None or len(arr) == 0:
        return 0
 
    max_sum = cur_sum = float('-inf')
    for num in arr:
        if cur_sum <= 0:
            cur_sum = num
        else:
            cur_sum += num
        if cur_sum > max_sum:
            max_sum = cur_sum
 
    return max_sum


    
def find_max_matrix(matrix):
    max_sum = float('-inf')
    row = len(matrix)  

    for i in range(row):
        sum_arr = matrix[i]
        cur_sum = find_max(sum_arr)
        if cur_sum > max_sum:
            max_sum = cur_sum

        for j in range(i+1, row):
            sum_arr = [sum_arr[x]+matrix[j][x] for x in range(len(sum_arr))]
            cur_sum = find_max(sum_arr)
            if cur_sum > max_sum:
                max_sum = cur_sum
                    
    return max_sum
 
a=np.array([[0,-2,-7,0],[9,2,-6,2],[-4,1,-4,1],[-1,8, 0,-2]])
#b=np.array([-1,8,2,0,1,-5,7,1,-19,10,3])

find_max_matrix(a)
