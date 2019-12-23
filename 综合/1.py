# encoding: utf-8

import numpy as np


class eightPuzzle(object):
    directions = ['up', 'down', 'left', 'right']
    max = 7

    def __init__(self, arr, cost=0, parent=None):
        self.arr = arr
        self.cost = cost
        self.parent = parent

    def getCost(self):
        return self.cost

    def calc(self, state):
        final = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
        postion = np.where(state.arr == final)
        return len(state.arr[postion])

    def showInfo(self):
        for i in range(3):
            for j in range(3):
                print(self.arr[i, j], end='   ')
            print("\n")
        print('->')

    def calc2(self, state1, stop):
        for x in stop:
            postion = np.where(state1.arr == x.arr)
            if len(state1.arr[postion]) == 9:
                return True
        return False

    def SubStates(self):
        subStates = []
        row, col = np.where(self.arr == 0)
        for direction in self.directions:
            if 'left' == direction and col > 0:
                s = self.arr.copy()
                s[row, col], s[row, col - 1] = s[row, col - 1], s[row, col]
                new = eightPuzzle(s, self.cost + 1, self)
                subStates.append(new)
            if 'up' == direction and row > 0:
                s = self.arr.copy()
                s[row, col], s[row - 1, col] = s[row - 1, col], s[row, col]
                new = eightPuzzle(s, self.cost + 1, self)
                subStates.append(new)
            if 'down' == direction and row < 2:
                s = self.arr.copy()
                s[row, col], s[row + 1, col] = s[row + 1, col], s[row, col]
                new = eightPuzzle(s, self.cost + 1, self)
                subStates.append(new)
            if 'right' == direction and col < 2:
                s = self.arr.copy()
                s[row, col], s[row, col + 1] = s[row, col + 1], s[row, col]
                new = eightPuzzle(s, self.cost + 1, self)
                subStates.append(new)
        return subStates

    def DFS(self):
        stack = []
        stop = []
        stack.append(self)
        count = -1
        while True:
            if not stack:
                return False, count, node
            count += 1
            node = stack.pop()
            stop.append(node)
            node.showInfo()
            if self.calc(node) == 9:
                return True, count, node
            s = node.SubStates()
            if s:
                res = sorted(s, key=self.calc)
            else:
                continue
            for x in res:
                if (x.cost + 9 - self.calc(x)) < eightPuzzle.max:
                    if self.calc2(x, stop):
                        continue
                    stack.append(x)


def showInfo(result):
    for node in result:
        for i in range(3):
            for j in range(3):
                print(node.arr[i, j], end='   ')
            print('\n')
        print('->')


def main():
    # start = np.array([[0, 1, 3], [8, 2, 4], [7, 6, 5]])
    start = np.array([[2, 8, 3], [1, 0, 4], [7, 6, 5]])
    p = eightPuzzle(start)
    res, count, node = p.DFS()
    result = []
    if res:
        print('经过%d次变换结束' % count)
        while node:
            result.append(node)
            node = node.parent
        result.reverse()
        showInfo(result)
    else:
        print('规定范围内未找到合适路径，可增大界值')


if __name__ == '__main__':
    main()