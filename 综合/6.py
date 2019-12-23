def cmp(x, y):
    return x > y


def dfs(ass, sum, g, p):
    if (sum * g == ans):
        print("%d\n", g)
        exit()
    if (ans - ass < a[cnt]):
        return
    if (ass == g):
        dfs(0, sum + 1, g, 1)

        return

    for i in range(p, cnt):
        if (~b[i] and ass + a[i] <= g):
            b[i] = 1
            dfs(ass + a[i], sum, g, i + 1)
            b[i] = 0
            if (ass + a[i] == g or ass == 0):
                break
            while (a[i] == a[i + 1]):
                i += 1


if __name__ == '__main__':
    N = 70
    a = []

    n = input()
    for i in range(int(n)):
        x = input()
        x = int(x)
        if (x <= 50):
            cnt += 1
            a[cnt] = x
            ans += a[cnt]
            s = max(a[cnt], s)

    sort(a + 1, a + cnt + 1, cmp)
    for i in range(s, ans / 2):
        if ans % i == 0:
            dfs(0, 0, i, 1)
        print("%d\n", ans)