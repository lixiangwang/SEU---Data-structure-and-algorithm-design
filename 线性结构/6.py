# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""

def find_maxlist(num_list):

    length=len(num_list)
    max_value=-10000000000
    tmp=0
    p = 0
    q = 0
    t= []
    for i in range(length):
        if tmp+num_list[i]<num_list[i]:
            p = i
            q=1
        else:
            q+=1
        tmp = max(tmp + num_list[i], num_list[i])
        max_value=max(max_value, tmp)
        if tmp == max_value:
            t.append((p, (p + q)))
    start = t[-1][0]
    end = t[-1][1]
    display_list=[]
    for i in range(start,end):
        display_list.append(num_list[i])
        
    print('最大和子序列为:',display_list)
    print('最大和为:',max_value)
    
if __name__ == '__main__':
    a= [1, -2, 3, 10, -4, 7, 2, -5]
    find_maxlist(a)