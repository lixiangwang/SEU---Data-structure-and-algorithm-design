# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""

## 3.
class ReorderLink:
    @staticmethod
    def find_mid_node(head):
        if head is None or head.next is None:
            return head
        fast = head
        slow = head
        prev = slow
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        return slow  

    @staticmethod
    def reverse(head):  
        p = head
        if p is None or p.next is None:
            return p
        q = p
        p = p.next
        while p is not None:
            tmp = p.next
            p.next = q
            if q == head:
                q.next = None
            q = p
            p = tmp
        return q

    @staticmethod
    def reorder(head1, head2):
        cur1 = head1
        cur2 = head2
        tmp = None
        while cur1.next is not None:
            tmp = cur1.next
            cur1.next = cur2
            cur1 = tmp

            tmp = cur2.next
            cur2.next = cur1
            cur2 = tmp

        cur1.next = cur2  

    def __call__(self, link_head):
        before = link_head
        rest =self.find_mid_node(before)
        rest = self.reverse(rest)  
        self.reorder(before, rest)
        return link_head
    
    
class Node:  
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkList: 
    def __init__(self):
        self.head = None

    def append(self, x):
        if self.head is None:
            self.head = Node(x)
            return self
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(x)
        return self
    
link1 = LinkList()
link1.append(1).append(2).append(3).append(4).append(5).append(6)

head9 = link1.head

p = head9
print("排序前： ", end=" ")
while p is not None:
    print(p.data, end="\t")
    p = p.next

instance = ReorderLink()  
head9 = instance(head9)  
print()

p = head9
print("排序后： ", end=" ")
while p is not None:
    print(p.data, end="\t")
    p = p.next