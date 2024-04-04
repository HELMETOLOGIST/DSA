class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)
        return root
    
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self._min_value_node(root.right)
                root.key = successor.key
                root.right = self._delete_recursive(root.right, successor.key)
        return root
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root.key if root else None
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)
    
    def inorder_traversal(self):
        return self._inorder_recursive(self.root)
    
    def _inorder_recursive(self, root):
        result = []
        if root:
            result.extend(self._inorder_recursive(root.left))
            result.append(root.key)
            result.extend(self._inorder_recursive(root.right))
        return result
    
    def preorder_traversal(self):
        return self._preorder_recursive(self.root)
    
    def _preorder_recursive(self, root):
        result = []
        if root:
            result.append(root.key)
            result.extend(self._preorder_recursive(root.left))
            result.extend(self._preorder_recursive(root.right))
        return result
    
    def postorder_traversal(self):
        return self._postorder_recursive(self.root)
    
    def _postorder_recursive(self, root):
        result = []
        if root:
            result.extend(self._postorder_recursive(root.left))
            result.extend(self._postorder_recursive(root.right))
            result.append(root.key)
        return result
    
    def minimum(self):
        if self.root is None:
            return None
        node = self.root
        while node.left is not None:
            node = node.left
        return node.key
    
    def maximum(self):
        if self.root is None:
            return None
        node = self.root
        while node.right is not None:
            node = node.right
        return node.key
    
    def find_closest_value(self, target):
        closest = float('inf')  # Initialize closest to positive infinity
        return self._find_closest_value_recursive(self.root, target, closest)
    
    def _find_closest_value_recursive(self, node, target, closest):
        if node is None:
            return closest
        if abs(node.key - target) < abs(closest - target):
            closest = node.key
        if target < node.key:
            return self._find_closest_value_recursive(node.left, target, closest)
        elif target > node.key:
            return self._find_closest_value_recursive(node.right, target, closest)
        else:
            return closest
        
    def is_valid_bst(self):
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_valid_bst_recursive(self, node, min_val, max_val):
        if node is None:
            return True
        
        if node.key <= min_val or node.key >= max_val:
            return False
        
        return (self._is_valid_bst_recursive(node.left, min_val, node.key) and
                self._is_valid_bst_recursive(node.right, node.key, max_val))
        

# Example usage:
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder traversal:", bst.inorder_traversal())
print("Preorder traversal:", bst.preorder_traversal())
print("Postorder traversal:", bst.postorder_traversal())

print("Minimum element:", bst.minimum())
print("Maximum element:", bst.maximum())
 
print("Closet Value:", bst.find_closest_value(90))

bst.delete(30)
print("Inorder traversal after deleting 30:", bst.inorder_traversal())

print("Searching for 40:", bst.search(40))

print("valid bst:", bst.is_valid_bst())
