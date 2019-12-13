# encoding: utf-8
"""
@author:  wanglixiang
@contact: lixiangwang9705@gmail.com
"""

class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return len(self.items)==0 
 
    def push(self, item):
        self.items.append(item)
 
    def pop(self):
        if not self.is_empty():
            return self.items.pop() 
 
    def top(self):
        if not self.is_empty():
            return self.items[len(self.items)-1]
 
    def size(self):
        return len(self.items)
    
    def print_stack(self):
        for sl in self.items:
            print(sl)
        


def solve(s):
    if s.is_empty():
        return
    
    top=s.top()
    s.pop()
    
    solve(s)
    
    if s.is_empty():
        s.push(top)
        return
    
    top2=s.top()
    s.pop()
    
    if top>top2:
        s.push(top)
        solve(s)
        s.push(top2)
    else:
        s.push(top2)
        s.push(top)
        

stack=Stack()
stack.push(5)
stack.push(1)
stack.push(4)
stack.push(3)
stack.push(2)
print('排序之前：')
stack.print_stack()
solve(stack)
print('排序之后：')
stack.print_stack()