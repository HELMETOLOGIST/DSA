class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

def insert(root,newValue):
    if root is None: 
        root = BinaryTree(newValue)
        return root
    if newValue < root.data:
        root.lchild = insert(root.lchild, newValue)
    else:
        root.rchild = insert(root.rchild, newValue)
    return root

def search(root, value):
    if root is None:
        return False
    if root.data == value:
        return True
    elif root.data > value:
        return search(root.lchild,value)
    else:
        return search(root.rchild,value)
    
root = insert(None, 50)
insert(root,9)
insert(root,67)
insert(root,33)
insert(root,21)
insert(root,98)
insert(root,43)
insert(root,73)
print(search(root,21))
print(search(root,100))
print(root.data)