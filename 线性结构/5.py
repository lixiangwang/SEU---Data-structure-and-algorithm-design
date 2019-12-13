# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""

def mins(a,b,c):
    mins = a if a < b else b
    mins = mins if mins < c else c
    return mins
 
def maxs(a,b,c):
    maxs = b if a < b else a
    maxs = c if maxs < c else maxs
    return maxs
 
def minDistance(a,b,c):
    aLen = len(a)
    bLen = len(b)
    cLen = len(c)
    curDist = 0
    minsd = 0
    minDist = 2 ** 32
    best_i = i = 0   
    best_j = j = 0   
    best_k = k = 0   
    while True:
        curDist = maxs(abs(a[i]-b[j]),abs(a[i]-c[k]),abs(b[j]-c[k]))
        if curDist < minDist:
            minDist = curDist
            best_i = i
            best_j = j
            best_k = k
        
        minsd = mins(a[i],b[j],c[k])
        if minsd == a[i]:
            i += 1
            if i >= aLen:
                break
        elif minsd == b[j]:
            j += 1
            if j >= bLen:
                break
        else:
            k += 1
            if k >= cLen:
                break
    return (a[best_i] , b[best_j], c[best_k])
 
if __name__ == "__main__":
    a = [3,4,5,7,15]
    b = [10,12,14,16,17]
    c = [20,21,23,24,37,30]
    
    (best_a, best_b, best_c) = minDistance(a,b,c)
    
    print('满足条件的三元组为：',(best_a, best_b, best_c))
