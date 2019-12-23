# encoding: utf-8



class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.maxSum = float('-inf')

    def findMaxSubTree(self, root, maxRoot):
        if root == None:
            return 0
        lmax = self.findMaxSubTree(root.left , maxRoot)
        rmax = self.findMaxSubTree(root.right, maxRoot)
        sums = lmax + rmax + root.value

        if sums > self.maxSum:
            self.maxSum = sums
            maxRoot.value = root.value
        return sums

    def constructTree(self):
        root = Node(-4)

        root.left = Node(-2)
        root.right = Node(3)

        root.right.left =Node(2)
        root.right.right = Node(-5)
        root.left.left = Node(11)

        root.right.right.right = Node(4)
        root.left.left.left = Node(-3)
        root.left.left.right = Node(11)

        return root


if __name__ == "__main__":
    solution = Solution()
    root = solution.constructTree()

    maxRoot = Node(None)
    solution.findMaxSubTree(root, maxRoot)
    print("最大子树和为：" + str(solution.maxSum))
    print("对应子树的根节点为：" + str(maxRoot.value))