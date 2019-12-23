import time

time_count = time.clock()
p, x, flower= [i**21 for i in range(10)], [int(i) for i in str(int(9*1e20))], []
f = lambda x: sum(p[b] for b in x)
while(x[0] > 7):
    y = f(x)
    v = 1e20 < y < 1e21
    if v and sorted(x) == sorted(int(i) for i in str(y)):   flower.append(y)
    try:    k = x.index(0)
    except:
        try:    k = x.index(1)
        except: x[-1] -= 1
        else:
            x[k-1] -= 1
            for j in range(k,len(x)):   x[j] = 0
    else:
        if v:   x[k] = x[k-1]
        else:   x[k-1] -= 1
print(sorted(flower),'\nTime : ',int(time.clock()-time_count),'s')