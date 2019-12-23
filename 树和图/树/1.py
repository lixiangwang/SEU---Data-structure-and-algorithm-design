# encoding: utf-8

#from binarytree import Node    ##binarytree的Node可以print可视化

class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: Node, first=True) -> bool:
        if not root: return first or 0
        l, r = map(lambda x: self.isBalanced(x, False), [root.left, root.right])
        return max(l,r)+1 if min(l,r)>-1 and abs(l-r)<=1 else (-1, False)[first]


if __name__ == '__main__':
    solution = Solution()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.left = Node(5)

    # print(root)
    result = solution.isBalanced(root)
    if result == False:
        print('此二叉树非平衡')
    else:
        print('此二叉树非平衡')



