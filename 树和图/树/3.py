# encoding: utf-8

#from binarytree import Node    ##binarytree的Node可以print可视化
class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root: Node) -> int:
        if not root:
            return 0
        self.depth(root)
        return self.ans

    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        if left + right > self.ans:
            self.ans = left + right
        return 1 + max(left, right)


if __name__ == '__main__':
    solution = Solution()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.left = Node(5)

    print('该二叉树的直径为：',solution.diameterOfBinaryTree(root))

