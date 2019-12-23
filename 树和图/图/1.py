# encoding: utf-8

def floyd(arr,n,startP,endP):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if arr[i][j]>(arr[i][k]+arr[k][j]) and i !=j:
                    arr[i][j] = arr[i][k] + arr[k][j]
    return arr[startP-1][endP-1],arr

if __name__ == '__main__':
    n = 6
    arr = [[float('inf')] * n for _ in range(n)]
    arr[0][1] = 6
    arr[0][2] = 3
    arr[1][2] = 2
    arr[1][3] = 5
    arr[2][3] = 3
    arr[2][4] = 4
    arr[3][4] = 2
    arr[3][5] = 3
    arr[4][5] = 5

    for i in range(n):
        arr[i][i] = 0.0
        for j in range(n):
            if arr[i][j] != 'inf':
                arr[j][i] = arr[i][j]
    print(floyd(arr,n,3,3))