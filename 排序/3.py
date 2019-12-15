# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        def partition(start, end):
            node = start.next.next
            pivotPrev = start.next
            pivotPrev.next = end
            pivotPost = pivotPrev
            while node != end:
                temp = node.next
                if node.val > pivotPrev.val:
                    node.next = pivotPost.next
                    pivotPost.next = node
                elif node.val < pivotPrev.val:
                    node.next = start.next
                    start.next = node
                else:
                    node.next = pivotPost.next
                    pivotPost.next = node
                    pivotPost = pivotPost.next
                node = temp
            return [pivotPrev, pivotPost]

        def quicksort(start, end):
            if start.next != end:
                prev, post = partition(start, end)
                quicksort(start, prev)
                quicksort(post, end)

        newHead = ListNode(0)
        newHead.next = head
        quicksort(newHead, None)
        return newHead.next

if __name__ == '__main__':
    solution = Solution()
    list0 = [22,44,87,50,18,42,21,96]
    stack = head = ListNode(None)
    for val in list0:
        stack.next = ListNode(val)
        stack = stack.next

    Sort_stack = solution.sortList(head.next)
    print('处理后的链表为：\n')
    while Sort_stack:
        print(Sort_stack.val)
        Sort_stack = Sort_stack.next
