# encoding: utf-8

def isBipartite(graph) -> bool:
    n = len(graph)
    record = [0] * n

    def dfs(point, c):
        record[point] = c
        for i in graph[point]:
            if record[i] == -c:
                continue
            elif record[i] == c:
                return False
            elif record[i] == 0 and not dfs(i, -c):
                return False
        return True

    for i in range(n):
        if record[i] == 0 and not dfs(i, 1):
            return False
    return True


if __name__ == '__main__':
    # 定义图结构
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]

    print('是否为二分图：', isBipartite(graph))