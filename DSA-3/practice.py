# class BinaryTree:
#     def __init__(self, data):
#         self.data = data
#         self.child1 = None
#         self.child2 = None

# node1 = BinaryTree(10)
# node2 = BinaryTree(12)
# node3 = BinaryTree(9)
# node4 = BinaryTree(11)
# node5 = BinaryTree(8)
# node6 = BinaryTree(13)
# node7 = BinaryTree(7)

# node1.child1 = node2
# node1.child2 = node3
# node2.child1 = node4
# node2.child2 = node5
# node3.child1 = node6
# node3.child2 = node7

# print(f"Root Node:{node1.data}")
# print(f"Child1 is:{node1.child1.data}")
# print(f"Child2 is:{node1.child2.data}")
# print(f"Child1 is:{node2.child1.data}")
# print(f"Child2 is:{node2.child2.data}")
# print(f"Child1 is:{node3.child1.data}")
# print(f"Child2 is:{node3.child2.data}")




# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None


# def insert(root, newValue):
#     # if binary search tree is empty, create a new node and declare it as root
#     if root is None:
#         root = BinaryTreeNode(newValue)
#         return root
#     # if newValue is less than value of data in root, add it to left subtree and proceed recursively
#     if newValue < root.data:
#         root.leftChild = insert(root.leftChild, newValue)
#     else:
#         # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
#         root.rightChild = insert(root.rightChild, newValue)
#     return root


# def search(root, value):
#     # node is empty
#     if root is None:
#         return False
#     # if element is equal to the element to be searched
#     elif root.data == value:
#         return True
#     # element to be searched is less than the current node
#     elif root.data > value:
#         return search(root.leftChild, value)
#     # element to be searched is greater than the current node
#     else:
#         return search(root.rightChild, value)


# root = insert(None, 50)
# insert(root, 20)
# insert(root, 53)
# insert(root, 11)
# insert(root, 22)
# insert(root, 52)
# insert(root, 78)
# print("53 is present in the binary tree:", search(root, 53))
# print("100 is present in the binary tree:", search(root, 100))


# class BinaryTree:
#     def __init__(self,data):
#         self.data = data
#         self.lchild = None
#         self.rchild = None

# def insert(root,newValue):
#     if root is None: 
#         root = BinaryTree(newValue)
#         return root
#     if newValue < root.data:
#         root.lchild = insert(root.lchild, newValue)
#     else:
#         root.rchild = insert(root.rchild, newValue)
#     return root

# def search(root, value):
#     if root is None:
#         return False
#     if root.data == value:
#         return True
#     elif root.data > value:
#         return search(root.lchild,value)
#     else:
#         return search(root.rchild,value)
    
# root = insert(None, 50)
# insert(root,9)
# insert(root,67)
# insert(root,33)
# insert(root,21)
# insert(root,98)
# insert(root,43)
# insert(root,73)
# print(search(root,21))
# print(search(root,100))
# print(root.data)




# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None


# def preorder(root):
#     # if root is None,return
#     if root is None:
#         return
#     # print the current node
#     print(root.data, end=" ,")
#     # traverse left subtree
#     preorder(root.leftChild)

#     # traverse right subtree
#     preorder(root.rightChild)


# def insert(root, newValue):
#     # if binary search tree is empty, create a new node and declare it as root
#     if root is None:
#         root = BinaryTreeNode(newValue)
#         return root
#     # if newValue is less than value of data in root, add it to left subtree and proceed recursively
#     if newValue < root.data:
#         root.leftChild = insert(root.leftChild, newValue)
#     else:
#         # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
#         root.rightChild = insert(root.rightChild, newValue)
#     return root


# root = insert(None, 50)
# insert(root, 20)
# insert(root, 53)
# insert(root, 11)
# insert(root, 22)
# insert(root, 52)
# insert(root, 78)
# print("Preorder traversal of the binary tree is:")
# preorder(root)


# class BinaryTree:
#     def __init__(self,data):
#         self.data = data
#         self.leftchild = None
#         self.rightchild = None

# def preorder(root):
#     if root is None:
#         return
#     print(root.data, end=", ")
#     preorder(root.leftchild)
#     preorder(root.rightchild)

# def insert(root, value):
#     if root is None:
#         root = BinaryTree(value)
#         return root
#     elif value < root.data:
#         root.leftchild = insert(root.leftchild, value)
#     else:
#         root.rightchild = insert(root.rightchild, value)
#     return root

# root = insert(None,78)
# insert(root,43)
# insert(root,23)
# insert(root,12)
# insert(root,52)
# insert(root,89)
# insert(root,19)
# print(preorder(root))


# class BinaryTree:
#     def __init__(self,data):
#         self.data = data
#         self.LChild = None
#         self.RChild = None

# def postorder(root):
#     if root is None:
#         return
#     print(root.data, end=", ")
#     postorder(root.LChild)
#     postorder(root.RChild)

# def insert(root, value):
#     if root is None:
#         root = BinaryTree(value)
#         return root
    
#     elif value < root.data:
#         root.LChild = insert(root.LChild, value)
#     else:
#         root.RChild = insert(root.RChild, value)
#     return root

# root = insert(None, 78)
# insert(root,43)
# insert(root,23)
# insert(root,12)
# insert(root,52)
# insert(root,89)
# insert(root,19)
# print(postorder(root))



