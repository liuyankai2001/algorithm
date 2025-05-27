

class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root=None
        self.arr = []

    # 层序建树
    def build_tree(self,val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            if self.arr[0].left is None:
                self.arr[0].left = new_node

            else:
                self.arr[0].right = new_node
                self.arr.pop(0)
        self.arr.append(new_node)

    # 层序遍历
    def level_order(self):
        self.arr.clear()
        self.arr.append(self.root)
        while len(self.arr)>0:
            print(self.arr[0].val,end=' ')
            if self.arr[0].left is not None:
                self.arr.append(self.arr[0].left)
            if self.arr[0].right is not None:
                self.arr.append(self.arr[0].right)
            self.arr.pop(0)
        print("")

    # 前序遍历
    def pre_order(self,node):
        if node:
            print(node.val,end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)
    # 中序遍历
    def mid_order(self,node):
        if node:
            self.mid_order(node.left)
            print(node.val,end=" ")
            self.mid_order(node.right)

    # 后序遍历
    def rear_order(self, node):
        if node:
            self.rear_order(node.left)
            self.rear_order(node.right)
            print(node.val, end=" ")

if __name__ == '__main__':
    tree = Tree()
    for i in range(1,10):
        tree.build_tree(i)
    # tree.level_order()
    tree.pre_order(tree.root)
    print("")
    tree.mid_order(tree.root)
    print("")
    tree.rear_order(tree.root)
    print("")