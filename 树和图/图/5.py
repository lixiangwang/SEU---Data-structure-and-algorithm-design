# encoding: utf-8

def GraphColor(graph, start, coloring, color):
    if start not in graph:
        return False, {}

    if start not in coloring:
        coloring[start] = color
    elif coloring[start] != color:
        return False, {}
    else:
        return True, coloring

    if color == 'color_a':
        newcolor = 'color_b'
    else:
        newcolor = 'color_a'

    for vertex in graph[start]:
        val, coloring = GraphColor(graph, vertex, coloring, newcolor)
        if val == False:
            return False, {}

    return True, coloring


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

    print('该着色图为：', GraphColor(graph, '0', {}, 'Sha'))