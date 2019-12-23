# encoding: utf-8
def TopologicalSort(G, flag):
    in_degrees = dict((u, 0) for u in G)
    for u in G:
        for v in G[u]:
            in_degrees[v] += 1

    Q = [u for u in G if in_degrees[u] == 0]
    res = []

    while Q:
        u = Q.pop()
        if len(Q) == 0 or flag == 2:
            res.append(u)
        else:
            u2 = Q.pop()
            Q.append(u)
            res.append(u2)

        for v in G[u]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                Q.append(v)

    return res


if __name__ == '__main__':
    # 定义图结构
    graph = {
        "1": ["2", "4"],
        "2": ["5"],
        "3": ["1", "6"],
        "4": ["2", "6"],
        "5": [],
        "6": ["5"],
    }

    print('第一个拓扑系列：', TopologicalSort(graph, 1))
    print('第二个拓扑系列：', TopologicalSort(graph, 2))

