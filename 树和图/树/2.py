# encoding: utf-8


class Node(object):
    def __init__(self,name=None,value=None):
        self.name = name
        self.value=value
        self.left=None
        self.right=None


def HuffmanTree(char_weights):
    a=[Node(part[0],part[1]) for part in char_weights]
    while len(a)!=1:
        a.sort(key=lambda node:node.value,reverse=True)
        c=Node(value=(a[-1].value+a[-2].value))
        c.left=a.pop(-1)
        c.right=a.pop(-1)
        a.append(c)
    root=a[0]

    return root

def find_wpl(tree_node,length):
    if tree_node.left == None and tree_node.right ==None:
        result = tree_node.value*length
    else:
        result = find_wpl(tree_node.left,length+1) + find_wpl(tree_node.right,length+1)

    return result


if __name__=='__main__':
    #输入的是字符及其权
    char_weights=[('a',5),('b',4),('c',10),('d',8),('f',15),('g',2)]
    tree_root=HuffmanTree(char_weights)
    result = find_wpl(tree_root,0)

    print('树的带权路径长度为：',result)









