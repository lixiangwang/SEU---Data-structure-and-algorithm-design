# encoding: utf-8

def findAllPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = findAllPath(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


if __name__ == '__main__':
    # 定义图结构
    graph = {
        "0": ["1", "2", "3"],
        "1": ["4"],
        "2": ["4", "5"],
        "3": ["5"],
        "4": ["6", "7"],
        "5": ["7"],
        "6": ["8"],
        "7": ["8"],
        "8": [],
    }

    print('图中0到8的所有路径为：', findAllPath(graph, "0", "8"))