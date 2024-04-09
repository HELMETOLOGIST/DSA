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


# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
        
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def insert(self,key):
#         self.root = self.insert_recursive(self.root,key)

#     def insert_recursive(self, root, key):
#         if root is None:
#             return TreeNode(key)
#         if key < root.key:
#             root.left = self.insert_recursive(root.left, key)
#         else:
#             root.right = self.insert_recursive(root.right, key)
#         return root
    
#     def delete(self,key):
#         self.root = self.delete_recursive(self.root, key)

#     def delete_recursive(self, root, key):
#         if root is None:
#             return root
#         if key < root.key:
#             root.left = self.delete_recursive(root.left, key)
#         elif key > root.key:
#             root.right = self.delete_recursive(root.right. key)
#         else:
#             if root.left is None:
#                 return root.right
#             elif root.right is None:
#                 return root.left
#             else:
#                 succes = self.min_value_node(root.right)
#                 root.key = succes.key
#                 root.right = self.delete_recursive(root.right, succes.key)
#         return root
    
#     def min_value_node(self,node):
#         current = node
#         while current.left is not None:
#             current = current.left
#         return current
    
#     def search(self, key):
#         return self.search_recursive(self.root, key)
    
#     def search_recursive(self, root, key):
#         if root is None or key == root.key:
#             return root
#         if key < root.key:
#             return self.search_recursive(root.left, key)
#         return self.search_recursive(root.right, key)
    
#     def inorder(self):
#         return self.inorder_recursive(self.root)
    
#     def inorder_recursive(self, root):
#         result = []
#         if root:
#             result.extend(self.inorder_recursive(root.left))
#             result.append(root.key)
#             result.extend(self.inorder_recursive(root.right))
#         return result
    
#     def preorder(self):
#         return self.preorder_recursive(self.root)
    
#     def preorder_recursive(self, root):
#         result = []
#         if root:
#             result.append(root.key)
#             result.extend(self.preorder_recursive(root.left))
#             result.extend(self.preorder_recursive(root.right))
#         return result
    
#     def postorder(self):
#         return self.postorder_recursive(self.root)
    
#     def postorder_recursive(self, root):
#         result = []
#         if root:
#             result.extend(self.postorder_recursive(root.left))
#             result.extend(self.postorder_recursive(root.right))
#             result.append(root.key)
#         return result
    
#     def minimum(self):
#         if self.root is None:
#             return None
#         node = self.root
#         while node.left is not None:
#             node = node.left
#         return node.key
    
#     def maximum(self):
#         if self.root is None:
#             return None
#         node = self.root
#         while node.right is not None:
#             node = node.right
#         return node.key
    


# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class BinarySTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, key):
#         self.root = self.insert_recursive(self.root,key)
#     def insert_recursive(self, root, key):
#         if self.root is None:
#             return TreeNode(key)
#         if key < root.key:
#             root.left = self.insert_recursive(root.left, key)
#         else:
#             root.right = self.insert_recursive(root.right, key)
#         return root
    
#     def delete(self, key):
#         self.root = self.delete_recursive(self.root, key)
#     def delete_recursive(self, root, key):
#         if root is None:
#             return root
#         if key < root.key:
#             root.left = self.delete_recursive(root.left, key)
#         elif key > root.key:
#             root.right = self.delete_recursive(root.right, key)
#         else:
#             if root.left is None:
#                 return root.right
#             elif root.right is None:
#                 return root.left
#             else:
#                 suppressor = self.min_val_node(root.right)
#                 root.key = suppressor.key
#                 root.right = self.delete_recursive(root.right, suppressor.key)
#         return root
#     def min_value_node(self, node):
#         current = node
#         while current.left is not None:
#             current = current.left
#         return current
    
#     def search(self, key):
#         return self.search_recursive(self.root, key)
#     def search_recursive(self, root, key):
#         if root is None or root.key == key:
#             return root.key if root else None
#         if key < root.key:
#             return self.search_recursive(root.left, key)
#         return self.search_recursive(root.right, key)
    
#     def inorder(self):
#         return self.inorder_recursive(self.root)
#     def inorder_recursive(self, root):
#         result = []
#         if root:
#             result.extend(self.inorder_recursive(root.left))
#             result.append(root.key)
#             result.extend(self.inorder_recursive(root.right))
#         return result
    
#     def postorder(self):
#         return self.postorder_recursive(self.root)
#     def postorder_recursive(self, root):
#         result = []
#         if root:
#             result.extend(self.postorder_recursive(root.left))
#             result.extend(self.postorder_recursive(root.right))
#             result.append(root.key)
#         return result
    
#     def preorder(self):
#         return self.preorder_recursive(self.root)
#     def preorder_recursive(self, root):
#         result = []
#         if root:
#             result.append(root.key)
#             result.extend(self.preorder_recursive(root.left))
#             result.extend(self.preorder_recursive(root.right))
#         return result
    
#     def minimum(self):
#         if self.root is None:
#             return None
#         node = self.root
#         while node.left is not None:
#             node = node.left
#         return node.key
#     def maximum(self):
#         if self.root is None:
#             return None
#         node = self.root
#         while node.right is not None:
#             node = node.right
#         return node.key
    
#     def find_closet_value(self, target):
#         closet = float('inf')
#         return self.find_closet_value_recursive(self.root, target, closet)
#     def find_closet_value_recursive(self, root, target, closet):
#         if root is None:
#             return closet
#         if abs(root.key - target) < abs(closet - target):
#             closet = root.key
#         if target < root.key:
#             return self.find_closet_value_recursive(root.left, target, closet)
#         elif target > root.key:
#             return self.find_closet_value_recursive(root.right, target, closet)
#         else:
#             return closet
     
#     def is_valid_bst(self):
#         return self.is_valid_bst_recursive(self.root, float('-inf'), float('inf'))
#     def is_valid_bst_recursive(self, root, minval, maxval):
#         if root is None:
#             return None
#         if root.key <= minval or root.key >= maxval:
#             return False
#         return (self.is_valid_bst_recursive(root.left, minval, root.key) and 
#                 self.is_valid_bst_recursive(root.right, root.key, maxval))


# class MinHeap:
#     def __init__(self):
#         self.heap = []

#     def build_heap(self, arr):
#         self.heap = arr[:]
#         n = len(self.heap)

#         for i in range(n//2, -1, -1):
#             self.heap_down(i)
#     def insert(self, value):
#         self.heap.append(value)
#         self.heap_up(len(self.heap)-1)

#     def heap_up(self, index):
#         parent = (index-1)//2

#         while index > 0 and self.heap[parent] > self.heap[index]:
#             self.swap(parent, index)
#             index = parent
#             parent = (index-1)//2

#     def heap_down(self, index):
#         left_child = (2*index) + 1
#         right_child = (2*index) + 2
#         smallest = index

#         if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
#             smallest = left_child
#         if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
#             smallest = right_child
#         if smallest != index:
#             self.swap(index, smallest)
#             self.heap_down(smallest)

#         def swap(self, i, j):
#             self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

#         def remove(self):
#             if not self.heap:
#                 return None
#             if len(self.heap) == 1:
#                 return self.heap.pop()
            
#             self.swap(0, len(self.heap)-1)
#             self.heap.pop()
#             self.heap_down(0)
#             return


# class MinHeap:
#     def __init__(self):
#         self.heap = []
#     def build_heap(self,arr):
#         self.heap = arr[:]
#         n = len(self.heap)

#         for i in range(n//2, -1, -1):
#             self.heap_down(i)

#     def insert(self, val):
#         self.heap.append(val)
#         self.heap_up(len(self.heap)-1)
#     def heap_up(self,index):
#         parent = (index - 1)//2

#         while index > 0 and self.heap[parent] > self.heap[index]:
#             self.swap(parent, index)
#             index = parent
#             parent = (index - 1)//2

#     def heap_down(self, index):
#         left = (2*index) + 1
#         right = (2*index) + 2
#         smallest = index

#         if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
#             smallest = left
#         if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
#             smallest = right
#         if smallest != index:
#             self.swap(index, smallest)
#             self.heap_down(smallest)

#     def swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

#     def remove(self):
#         if not self.head:
#             return None
#         if len(self.heap) == 1:
#             return self.heap.pop()
        
#         self.swap(0, len(self.heap) -1)
#         self.heap.pop()
#         self.heap_down(0)

# class MinHeap:
#     def __init__(self):
#         self.heap = []
    
#     def build_heap(self,arr):
#         self.heap = arr[:]
#         n = len(self.heap)
#         for i in range(n//2, -1,-1):
#             self.heap_down(i)
#     def insert(self, val):
#         self.heap.append(val)
#         self.heap_up(len(self.heap)-1)
#     def heap_up(self,index):
#         parent = (index - 1)//2

#         while index > 0 and self.heap[parent] > self.heap[index]:
#             self.swap(parent, index)
#             index = parent
#             parent = (index - 1)//2
#     def heap_down(self,index):
#         left = (2*index) + 1
#         right = (2*index) + 2
#         smallest = index

#         if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
#             smallest = left
#         if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
#             smallest = right
#         if smallest != index:
#             self.swap(index, smallest)
#             self.heap_down(smallest)
#     def swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

#     def remove(self):
#         if not self.heap:
#             return None
#         if len(self.heap) == 1:
#             return self.heap.pop()
#         self.heap(0, len(self.heap)-1)
#         self.heap.pop()
#         self.heap_down(0)
#         return


# class MinHeap:
#     def __init__(self):
#         self.heap = []
#     def build_heap(self,arr):
#         self.heap = arr[:]
#         n = len(self.heap)
#         for i in range(n//2,-1,-1):
#             self.heap_down(i)
#     def insert(self,val):
#         self.heap.append(val)
#         self.heap_up(len(self.heap)-1)
#     def heap_up(self, index):
#         parent = (index - 1)//2
#         while index > 0 and self.heap[parent] > self.heap[index]:
#             self.swap(parent, index)
#             index = parent
#             parent = (index - 1)//2
#     def heap_down(self,index):
#         left = (2*index) + 1
#         right = (2*index) + 2
#         smallest = index

#         if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
#             smallest = left
#         if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
#             smallest = right
#         if smallest != index:
#             self.swap(index, smallest)
#             self.heap_down(smallest)
#     def swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

#     def remove(self):
#         if not self.heap:
#             return None
#         if len(self.heap) == 1:
#             return self.heap.pop()
#         self.swap(0, len(self.heap)-1)
#         self.heap.pop()
#         self.heap_down(0)
#         return
 

# def heap_sort(arr):
#     n = len(arr)
#     for i in range(n//2, -1, -1):
#         heapify(arr, n, i)
    
#     for i in range(n-1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, i, 0)
#     return print(arr)
# def heapify(arr, n, index):
#     left = (2*index) + 1
#     right = (2*index) + 2
#     largest = index
#     if left < n and arr[left] > arr[largest]:
#         largest = left
#     if right < n and arr[right] > arr[largest]:
#         largest = right
#     if largest != index:
#         arr[largest], arr[index] = arr[index], arr[largest]
#         heapify(arr,n,largest)
# array = [7,65,5,3,68,75,63]
# heap_sort(array)


# def heap_sort(arr):
#     n = len(arr)
#     for i in range(n//2, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n-1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, i, 0)
#     return print(arr)
# def heapify(arr, n, index):
#     left = (2*index) + 1
#     right = (2*index) + 2
#     largest = index
#     if left < n and arr[left] > arr[largest]:
#         largest = left
#     if right < n and arr[right] > arr[largest]:
#         largest = right
#     if largest != index:
#         arr[largest], arr[index] = arr[index], arr[largest]
#         heapify(arr, n, largest)
# arr = [9,8,76,54,4,5,6]
# heap_sort(arr)


# def heap_sort(arr):
#     n = len(arr)
#     for i in range(n//2, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n-1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, 0, i)
#     return print(arr)
# def heapify(arr, n, index):
#     left = (2*index) + 1
#     right = (2*index) + 2
#     largest = index
#     if left < n and arr[left] > arr[largest]:
#         largest = left
#     if right < n and arr[right] > arr[largest]:
#         largest = right
#     if largest != index:
#         arr[largest], arr[index] = arr[index], arr[largest]
#         heapify(arr, n, largest)


# def heap_sort(arr):
#     n = len(arr)
#     for i in range(n//2, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n-1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, i, 0)
#     return print(arr)
# def heapify(arr, n, index):
#     left = (2*index) + 1
#     right = (2*index) + 2
#     largest = index
#     if left < n and arr[left] > arr[largest]:
#         largest = left
#     if right < n and arr[right] > arr[largest]:
#         largest = right
#     if largest != index:
#         arr[largest], arr[index] = arr[index], arr[largest]
#         heapify(arr, n, largest)



# def heap_sort(arr):
#     n = len(arr)
#     for i in range(n//2, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n-1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[i]
#         heapify(arr, i, 0)
#     return print(arr)
# def heapify(arr, n, index):
#     left = (2*index) + 1
#     right = (2*index) + 2
#     largest = index
#     if left < n and arr[left] > arr[largest]:
#         largest = left
#     if right < n and arr[right] > arr[largest]:
#         largest = right
#     if largest != index:
#         arr[largest], arr[index] = arr[index], arr[largest]
#         heapify(arr, n, largest)
# array = [4,56,12,37,89,19]
# heap_sort(array)


# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
# class BinarySTree:
#     def __init__(self):
#         self.root = None
#     def insert(self, key)
#         self.root = self.insert_recursive(self.root, key)
#     def insert_recursive(self, root, key):
#         if root is None:
#             return TreeNode(key)
#         if key < root.key:
#             root.left = self.insert_recursive(root.left, key)
#         else:
#             root.right = self.insert_recursive(root.right, key)
#         return root

# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
# class BinarySTree:
#     def __init__(self):
#         self.root = None
#     def insert(self, key):
#         self.root = self.insert_recursive(self.root, key)
#     def insert_recursive(self, root, key):
#         if root is None:
#             return TreeNode(key)
#         if key < root.key:
#             root.left = self.insert_recursive(root.left, key)
#         else:
#             root.right = self.insert_recursive(root.right, key)
#         return root
#     def delete(self, key):
#         self.root = self.delete_recursive(self.root, key)
#     def delete_recursive(self, root, key):
#         if root is None:
#             return root
#         if key < root.key:
#             root.left = self.delete_recursive(root.left, key)
#         elif key > root.key:
#             root.right = self.delete_recursive(root.right, key)
#         else:
#             if root.left is None:
#                 return root.right
#             elif root.right is None:
#                 return root.left
#             else:
#                 success = self.min_value_node(root.right)
#                 root.key = success.key
#                 root.right = self.delete_recursive(root.right, success.key)
#         return root
#     def min_value_node(self, node):
#         curr = node
#         while curr.left is not None:
#             curr = curr.left
#         return curr


# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
# class BinarySTree:
#     def __init__(self):
#         self.root = None
#     def insert(self, key):
#         self.root = self.insert_recursive(self.root, key)
#     def insert_recursive(self, root, key):
#         if root is None:
#             return TreeNode(key)
#         if key < root.key:
#             root.left = self.insert_recursive(root.left, key)
#         else:
#             root.right = self.insert_recursive(root.right, key)
#         return root
#     def delete(self, key):
#         self.root = self.delete_recursive(self.root, key)
#     def delete_recursive(self, root, key):
#         if root is None:
#             return root
#         if key < root.key:
#             root.left = self.delete_recursive(root.left, key)
#         elif key > root.key:
#             root.right = self.delete_recursive(root.right, key)
#         else:
#             if root.left is None:
#                 return root.right
#             elif root.right is None:
#                 return root.left
#             else:
#                 success = self.min_value_node(root.right)
#                 root.key = success.key
#                 root.right = self.delete_recursive(root.right, success.key)
#         return root
#     def min_value_node(self, node):
#         curr = node
#         while curr.left is not None:
#             curr = curr.left
#         return curr
    

# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
# class BinarySTree:
#     def __init__(self):
#         self.root = None
#     def insert(self, key):
#         self.root = self.insert_recursive(self.root, key)
#     def insert_recursive(self, root, key):
#         if root is None:
#             return TreeNode(key)
#         if key < root.key:
#             root.left = self.insert_recursive(root.left, key)
#         else:
#             root.right = self.insert_recursive(root.right, key)
#         return root
#     def delete(self, key):
#         self.root = self.delete_recursive(self.root, key)
#     def delete_recursive(self, root, key):
#         if root is None:
#             return root
#         if key < root.key:
#             root.left = self.delete_recursive(root.left, key)
#         elif key > root.key:
#             root.right = self.delete_recursive(root.right, key)
#         else:
#             if root.left is None:
#                 return root.right
#             elif root.right is None:
#                 return root.left
#             else:
#                 success = self.min_value_node(root.right)
#                 root.key = success.key
#                 root.right = self.delete_recursive(root.right, success.key)
#         return root
#     def min_value_node(self, node):
#         curr = node
#         while curr.left is not None:
#             curr = curr.left
#         return curr
#     def search(self, key):
#         return self.search_recursive(self.root, key)
#     def search_recursive(self, root, key):
#         if root is None or if root.key == key:
#             return root.key if root else None
#         if key < root.key:
#             return self.search_recursive(root.left, key)
#         return self.search_recursive(root.right, key)
#     def inorder(self):
#         return self.inorder_recursive(self.root)
#     def inorder_recursive(self, root):
#         res = []
#         if root:
#             res.extend(self.inorder_recursive(root.left))
#             res.append(root.key)
#             res.extend(self.inorder_recursive(root.right))
#         return res
#     def preorder(self):
#         return self.preorder_recursive(self.root)
#     def preorder_recursive(self, root):
#         res = []
#         if root:
#             res.append(root.key)
#             res.extend(self.preorder_recursive(root.left))
#             res.extend(self.preorder_recursive(root.right))
#         return res
#     def postorder(self):
#         return self.postorder_recursive(self.root)
#     def postorder_recursive(self, root):
#         res = []
#         if root:
#             res.extend(self.postorder_recursive(root.left))
#             res.extend(self.postorder_recursive(root.right))
#             res.append(root.key)
#         return res


# class MinHeap:
#     def __init__(self):
#         self.heap = []
#     def build_heap(self, arr):
#         self.heap = arr[:]
#         n = len(self.heap)
#         for i in range(n//2, -1, -1):
#             self.heap_down(i)
#     def insert(self, val):
#         self.heap.append(val)
#         self.heap_up(len(self.heap)-1)
#     def heap_up(self, index):
#         parent = (index - 1)//2
#         while index > 0 and self.heap[parent] > self.heap[index]:
#             self.swap(parent, index)
#             index = parent
#             parent = (index - 1)//2
#     def heap_down(self, index):
#         left = (2*index) + 1
#         right = (2*index) + 2
#         smallest = index
#         if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
#             smallest = left
#         if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
#             smallest = right
#         if smallest != index:
#             self.swap(smallest, index)
#             self.heap_down(smallest)
#     def swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
#     def remove(self):
#         if not self.heap:
#             return None
#         if len(self.heap) == 1:
#             return self.heap.pop()
#         self.swap(0,len(self.heap)-1)
#         self.heap.pop()
#         self.heap_down(0)
#         return
    
# def heap_sort(arr):
#     n = len(arr)
#     for i in range(n//2, -1, -1):
#         heapify(arr, i, n)
#     for i in range(n-1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, i, 0)
#     return print(arr)
# def heapify(arr, n, index):
#     left = (2*index) + 1
#     right = (2*index) + 2
#     largest = index
#     if left < n and arr[left] > arr[largest]:
#         largest = left
#     if right < n and arr[right] > arr[largest]:
#         largest = right
#     if largest != index:
#         arr[largest], arr[index] = arr[index], arr[largest]
#         heapify(arr, n, largest)


# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
# class BST:
#     def __init__(self):
#         self.root = None
#     def insert(self, key):
#         self.root = self.insertRec(self.root, key)
#     def insertRec(self, root, key):
#         if root is None:
#             return TreeNode(key)
#         if key < root.key:
#             root.left = self.insertRec(root.left, key)
#         else:
#             root.right = self.insertRec(root.right, key)
#         return root
#     def delete(self, key):
#         self.root = self.deleteRec(self.root, key)
#     def deleteRec(self, root, key):
#         if root is None:
#             return root
#         if key < root.key:
#             root.left = self.deleteRec(root.left, key)
#         elif key > root.key:
#             root.right = self.deleteRec(root.right, key)
#         else:
#             if root.left is None:
#                 return root.right
#             elif root.right is None:
#                 return root.left
#             else:
#                 success = self.min_val_node(root.right)
#                 root.key = success.key
#                 root.right = self.deleteRec(root.right, success.key)
#         return root
#     def min_val_node(self, node):
#         curr = node
#         while curr.left is not None:
#             curr = curr.left
#         return curr
#     def search(self, key):
#         return self.searchRec(self.root, key)
#     def searchRec(self, root, key):
#         if root is None or root.key == key:
#             return root.key if root else None
#         if key < root.key:
#             return self.searchRec(root.left, key)
#         return self.searchRec(root.right, key)
#     def inorder(self):
#         return self.inorderRec(self.root)
#     def inorderRec(self, root):
#         res = []
#         if root:
#             res.extend(self.inorderRec(root.left))
#             res.append(root.key)
#             res.extend(self.inorderRec(root.right))
#         return res
#     def preorder(self):
#         return self.preorderRec(self.root)
#     def preorderRec(self, root):
#         res = []
#         if root:
#             res.append(root.key)
#             res.extend(self.preorderRec(root.left))
#             res.extend(self.preorderRec(root.right))
#         return res
#     def postorder(self):
#         return self.postorderRec(self.root)
#     def postorderRec(self, root):
#         res = []
#         if root:
#             res.extend(self.postorderRec(root.left))
#             res.extend(self.postorderRec(root.right)) 
#             res.append(root.key)
#         return res
#     def minimum(self):
#         if self.root is None:
#             return None
#         node = self.root
#         while node.left is not None:
#             node = node.left
#         return node.key
#     def maximum(self):
#         if self.root is None:
#             return None
#         node = self.root
#         while node.right is not None:
#             node = node.right
#         return node.key


# class MinHeap:
#     def __init__(self) -> None:
#         self.heap = []
#     def build_heap(self, arr):
#         self.heap = arr[:]
#         n = len(self.heap)
#         for i in range(n//2, -1, -1):
#             self.heap_down(i)
#     def insert(self, val):
#         self.heap.append(val)
#         self.heap_up(len(self.heap)-1)
#     def heap_up(self, index):
#         parent = (index - 1)//2
#         while index > 0 and self.heap[parent] > self.heap[index]:
#             self.swap(parent, index)
#             index = parent
#             parent = (index - 1)//2
#     def heap_down(self, index):
#         left = (2*index) + 1
#         right = (2*index) + 2
#         smallest = index
#         if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
#             smallest = left
#         elif right < len(self.heap) and self.heap[right] < self.heap[smallest]:
#             smallest = right
#         if smallest != index:
#             self.swap(smallest, index)
#             self.heap_down(smallest)
#     def swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
#     def remove(self):
#         if not self.heap:
#             return None
#         if len(self.heap) == 1:
#             return self.heap.pop()
#         self.swap(0, len(self.heap)-1)
#         self.heap.pop()
#         self.heap_down(0)
#         return

# def heap_sort(arr):
#     n = len(arr)
#     for i in range(n//2. -1, -1):
#         heapify(arr, n, i)
#     for i in range(n-1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, i, 0)
# def heapify(arr, n, index):
#     left = (2*index) + 1
#     right = (2*index) + 2
#     largest = index
#     if left < n and arr[left] > arr[largest]:
#         largest = left
#     elif right < n and arr[right] > arr[largest]:
#         largest = right
#     if largest != index:
#         arr[largest], arr[index] = arr[index], arr[largest]
#         heapify(arr, n, largest)
# arr = [56,7,8,9,76,5]

# class Graph:
#     def __init__(self):
#         self.graph = {}
#     def insert_vertex(self, vertex):
#         if vertex not in self.graph:
#             self.graph[vertex] = []
#     def add_edges(self, vertex, edge, bi=False):
#         self.insert_vertex(vertex)
#         self.insert_vertex(edge)
#         self.graph[vertex].append(edge)
#         if bi:
#             self.graph[edge].append(vertex)
#     def delete_vertex(self, vertex):
#         for vtx, edg in self.graph.items():
#             if vertex in edg:
#                 self.graph[vtx].remove(vertex)
#         del self.graph[vertex]

#     def BFS(self):
#         traversal = []
#         for vertex in self.graph:
#             if vertex not in traversal:
#                 queue = [vertex]

#                 while queue:
#                     node = queue.pop(0)
#                     if node not in traversal:
#                         traversal.append(node)

#                         for i in self.graph.get(node, []):
#                             if i not in traversal:
#                                 queue.append(i)
#         return traversal
#     def DFS(self):
#         traversal = []
#         def DFS_Util(vertex):
#             traversal.append(vertex)
#             for edge in self.graph.get(vertex, []):
#                 if edge not in traversal:
#                     DFS_Util(edge)
#         for vertex in self.graph:
#             if vertex not in traversal:
#                 DFS_Util(vertex)
#         return traversal

# class TrieNode:
#     def __init__(self) -> None:
#         self.children = {}
#         self.end_node = False
# class Trie:
#     def __init__(self) -> None:
#         self.root = TrieNode()
#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.end_node = True
#     def search(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return node.end_node
#     def starts_with(self, prefix):
#         node = self.root
#         for char in prefix:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return True