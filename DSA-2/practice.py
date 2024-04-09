# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
# arr = [45,39,87,45,33,74]
# bubble_sort(arr)
# print(arr)


# def bubble_sort_sl(arr):
#     for i in range(2):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
# arr = [7,65,42,34,59,8,5]
# bubble_sort(arr)
# print(arr[-2])


# def bubble_sorted_or_not(arr):
#     n = len(arr)
#     for i in range(n):
#         flag = 0
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 flag = 1
#         if flag == 0:
#             break

# arr = [1,2,3,4,53,6,7,8,9]
# bubble_sorted_or_not(arr)
# print(arr)



# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#         i += 1
# arr = [97,34,59,7,6,52]
# insertion_sort(arr)
# print(arr)


# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
# arr = [87,6,53,4,56,7,8,76]
# selection_sort(arr)
# print(arr)


# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
# arr = [67,53,48,75,6,82]
# selection_sort(arr)
# print(arr)


# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
# arr = [96,27,4,68,7,62,46]
# bubble_sort(arr)
# print("Bubble Sort:",arr)



# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#         i += 1
        
# arr = [96,27,4,68,7,62,46]
# insertion_sort(arr)
# print("Insertion Sort:",arr)


# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
# arr = [96,27,4,68,7,62,46]
# selection_sort(arr)
# print("Selection Sort:",arr)





# def merge_sort(arrr):
#     if len(arrr) <= 1:
#         return arrr
    
#     mid = len(arrr) // 2
#     left_h = arrr[:mid]
#     right_h = arrr[mid:]

#     left_h = merge_sort(left_h)
#     right_h = merge_sort(right_h)

#     return merge(left_h, right_h)

# def merge(left, right):
#     new = []
#     l_idx = 0
#     r_idx = 0

#     while l_idx < len(left) and r_idx < len(right):
#         if left[l_idx] < right[r_idx]:
#             new.append(left[l_idx])
#             l_idx += 1
#         else:
#             new.append(right[r_idx])
#             r_idx += 1

#     while l_idx < len(left):
#         new.append(left[l_idx])
#         l_idx += 1

#     while r_idx < len(right):
#         new.append(right[r_idx])
#         r_idx += 1

#     return new

# arrr = [4,58,71,28,90,3,45]
# sor = merge_sort(arrr)
# print(sor)

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def display(self):
#         if  not self.head:
#             print("Linked list is None")
#             return
#         else:
#             current = self.head 
#             while current:
#                 print(current.data, end="-->")
#                 current = current.next


#     def insert_begin(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node

    

# link = LinkedList()
# link.insert_begin(48)
# link.insert_begin(3)
# link.insert_begin(65)
# link.insert_begin(21)
# link.insert_begin(87)
# link.display()



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end="-->")
#             current = current.next
#         print()

#     def bubble_sort(self):
#         if self.head is None:
#             return
#         else:
#             swapped = True
#             while swapped:
#                 swapped = False
#                 current = self.head
#                 prev = None
#                 while current and current.next:
#                     if current.data > current.next.data:
#                         if prev:
#                             prev.next, current.next.next, current.next = current.next, prev.next, current.next.next
#                             swapped = True
#                         else:
#                             self.head, current.next.next, current.next = current.next, self.head, current.next.next
#                     prev, current = current, current.next
# # Create a linked list
# llist = LinkedList()
# arr = [45, 39, 87, 45, 33, 74]
# for num in arr:
#     llist.append(num)

# # Display the original linked list
# print("Original Linked List:")
# llist.display()

# # Sort the linked list using bubble sort
# llist.bubble_sort()

# # Display the sorted linked list
# print("Sorted Linked List:")
# llist.display()


# stack = []

# stack.append(10)
# stack.append(34)
# stack.append(22)
# stack.append(73)

# print(stack)

# print(stack.pop())
# print(stack.pop())


# print(stack)


# from collections import deque

# stack = deque()

# stack.append("Nijith")
# stack.append("Favas")
# stack.append("Asif")
# stack.append("Shibil")

# print(stack)


# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())


# print(stack)


# from queue import LifoQueue

# stack = LifoQueue(maxsize=4)

# stack.put("Nijith")
# stack.put("Favas")
# stack.put("Asif")
# stack.put("Shibil")

# print(stack.full())
# print(stack.qsize())

# print(stack.get())
# print(stack.get())
# print(stack.get())
# print(stack.get())


# print(stack.empty())


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
 
 
# class Stack:
 
#     # Initializing a stack.
#     # Use a dummy node, which is
#     # easier for handling edge cases.
#     def __init__(self):
#         self.head = Node("head")
#         self.size = 0
 
#     # String representation of the stack
#     def __str__(self):
#         cur = self.head.next
#         out = ""
#         while cur:
#             out += str(cur.value) + "->"
#             cur = cur.next
#         return out[:-2]
 
#     # Get the current size of the stack
#     def getSize(self):
#         return self.size
 
#     # Check if the stack is empty
#     def isEmpty(self):
#         return self.size == 0
 
#     # Get the top item of the stack
#     def peek(self):
 
#         # Sanitary check to see if we
#         # are peeking an empty stack.
#         if self.isEmpty():
#             raise Exception("Peeking from an empty stack")
#         return self.head.next.value
 
#     # Push a value into the stack.
#     def push(self, value):
#         node = Node(value)
#         node.next = self.head.next
#         self.head.next = node
#         self.size += 1
 
#     # Remove a value from the stack and return.
#     def pop(self):
#         if self.isEmpty():
#             raise Exception("Popping from an empty stack")
#         remove = self.head.next
#         self.head.next = self.head.next.next
#         self.size -= 1
#         return remove.value
 
 
# # Driver Code
# if __name__ == "__main__":
#     stack = Stack()
#     for i in range(1, 11):
#         stack.push(i)
#     print(f"Stack: {stack}")
 
#     for _ in range(1, 6):
#         remove = stack.pop()
#         print(f"Pop: {remove}")
#     print(f"Stack: {stack}")


# array = []

# array.append((2,"Nijith"))
# array.append((5,"Favas"))
# array.append((1,"Shibil"))
# array.append((3,"Sinan"))

# print(array)

# array.sort()
# print(array)

# while array:
#     next = array.pop()
#     print(next)


########### Insertion Sort ###########

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key 

# arr = [9,1,8,2,7,3,6,4]
# insertion_sort(arr)
# print("Insertion Sort:",arr)

# def Bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# arr = [15,6,8,34,51,20]
# Bubble_sort(arr)
# print(arr)

# def Bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# arr = [4,56,78,87,65,41,3]
# Bubble_sort(arr)
# print(arr)

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j+1] = key
# arr = [8,76,534,5,6,98]
# insertion_sort(arr)
# print(arr)


# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
# arr = [3,7,5,6,9,27,56,1]
# insertion_sort(arr)
# print(arr)

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[idx]:
#                 idx = j
#         arr[i], arr[idx] = arr[idx], arr[i]

# arr = [6,77,66,38,25,5,24]
# selection_sort(arr)
# print(arr)


# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[idx]:
#                 idx = j
#         arr[i], arr[idx] = arr[idx], arr[i]
# arr = [8,47,5,12,3,85,9,45]
# selection_sort(arr)
# print(arr)



# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[-1]
#     left = [x for x in arr[:-1] if x < pivot]
#     right = [x for x in arr[:-1] if x >= pivot]
#     return quick_sort(left)+[pivot]+quick_sort(right)

# arr = [9,87,65,43,21,23,45,67,8]
# q=quick_sort(arr)
# print(q)


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[-1]
#     left = [x for x in arr[:-1] if x < pivot]
#     right = [x for x in arr[:-1] if x >= pivot]
#     return quick_sort(left) + [pivot] + quick_sort(right)

# arr = [87,65,45,67,81,23]
# ans = quick_sort(arr)
# print(ans)

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     return merge(left, right)

# def merge(left,right):
#     merged = []
#     left_index = 0
#     right_index = 0

#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] < right[right_index]:
#             merged.append(left[left_index])
#             left_index += 1
#         else:
#             merged.append(right[right_index])
#             right_index += 1
        
#     while left_index < len(left):
#         merged.append(left[left_index])
#         left_index += 1
    
#     while right_index < len(right):
#         merged.append(right[right_index])
#         right_index += 1

#     return merged

# arr = [66,7,48,67,84,21,3,68]
# sortt = merge_sort(arr)
# print(sortt)

# class Queue:
#     def __init__(self):
#         self.item = []
#     def __str__(self):
#         arr_str = "-->".join([str(x) for x in self.item][::-1])
#         return "%s" % arr_str
#     def enqueue(self,x):
#         self.item.append(x)
#     def dequeue(self):
#         self.item.pop(0)
# def start():
#     q = Queue()
#     q.enqueue(3)
#     q.enqueue(1)
#     q.enqueue(9)
#     q.enqueue(6)
#     q.dequeue()
#     print(q)
# start()


# Queue Array Method
# class Queue:
#     def __init__(self):
#         self.items = []
#     def __str__(self):
#         srt = "-->".join([str(x) for x in self.items])
#         return "%s" % srt
#     def enqueue(self,x):
#         self.items.append(x)
#     def dequeue(self):
#         self.items.pop(0)

# def Start():
#     q = Queue()
#     q.enqueue(4)
#     q.enqueue(7)
#     q.enqueue(8)
#     q.enqueue(2)
#     q.enqueue(9)
#     q.dequeue()
#     print(q)
# Start()


# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
# class Stack:
#     def __init__(self):
#         self.head = Node("head")
#         self.size = 0

#     def __str__(self):
#         curr = self.head.next
#         res = ''
#         while curr:
#             res += str(curr.value) + '-->'
#             curr = curr.next
#         return res
    
#     def is_Empty(self):
#         return self.size == 0
    
#     def push(self,value):
#         node = Node(value)
#         node.next = self.head.next
#         self.head.next = node
#         self.size += 1

#     def pop(self):
#         if self.is_Empty():
#             raise Exception("Stack is empty")
#         current = self.head.next
#         self.head.next = self.head.next.next
#         self.size -= 1
#         return current.value
    
#     def peek(self):
#         if self.is_Empty():
#             raise Exception("Stack is empty")
        
#         return self.head.next.value
    
#     def getSize(self):
#         return self.size
    
# stk = Stack()
# stk.push(5)
# stk.push(8)
# stk.push(2)
# stk.push(4)
# stk.push(98)
# stk.push(12)
# print(f"stack {stk}")
# stk.pop()
# stk.pop()
# print(f"pop {stk}")


# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
# class Stack:
#     def __init__(self):
#         self.head = Node("head")
#         self.size = 0
#     def __str__(self):
#         cur = self.head.next
#         res = ''
#         while cur:
#             res += str(cur.value) + '-->'
#             cur = cur.next
#         return res
    
#     def isEmpty(self):
#         return self.size == 0
    
#     def getSize(self):
#         return self.size
    
#     def push(self,value):
#         node = Node(value)
#         node.next = self.head.next
#         self.head.next = node
#         self.size += 1

#     def pop(self):
#         if self.isEmpty():
#             raise Exception("stack empty")
#         current = self.head.next
#         self.head.next = self.head.next.next
#         self.size -= 1
#         return current.value
    
#     def peek(self):
#         if self.isEmpty():
#             raise Exception("stack is empty")
        
#         return self.head.next.value


# class Stack:
#     def __init__(self,value):
#         self.value = value
#         self.size = 0
#     def __str__(self):
#         return '-->'.join(map(str, self.value[::-1]))
#     def isEmpty(self):
#         return self.size == 0
#     def getSize(self):
#         if self.isEmpty():
#             raise Exception("stack is empty")
#         return self.size
#     def push(self,value):
#         self.value.append(value)
#         self.size += 1
#     def pop(self):
#         if self.isEmpty():
#             raise Exception("stack is empty")
#         self.size -= 1
#         return self.value.pop()
#     def peek(self):
#         if self.isEmpty():
#             raise Exception("stack is empty")
#         return self.value[-1]

# class Node:
#     def __init__(self,key,value):
#         self.key = key
#         self.value = value
#         self.next = None
# class HashTable:
#     def __init__(self,size):
#         self.size = size
#         self.table = [None] * size
#     def hash_function(self,key):
#         return hash(key) % self.size
    
#     def put(self,key,value):
#         index = self.hash_function(key)
#         if not self.table[index]:
#             self.table[index] = Node(key,value)
#         else:
#             node = self.table[index]
#             while node.next:
#                 if node.key == key:
#                     node.value = value
#                     return
#                 node = node.next
#             node.next = Node(key, value)

#     def get(self, key):
#         index = self.hash_function(key)
#         node = self.table[index]
#         while node:
#             if node.key == key:
#                 return node.value
#             node = node.next
#         raise KeyError("Key not found")
    
#     def remove(self, key):
#         index = self.hash_function(key)
#         if not self.table[index]:
#             raise KeyError("Key not found")
#         if self.table[index].key == key:
#             self.table[index] = self.table[index].next
#             return
#         prev = None
#         curr = self.table[index]
#         while curr:
#             if curr.key == key:
#                 prev.next = curr.next
#                 return
#             prev = curr
#             curr = curr.next
#         raise KeyError("Key not found")
    
# ht = HashTable(10)
# ht.put("apple",8)
# ht.put(7,"banana")
# ht.put(5,"orange")
# ht.put(3,"grapefruit")
# ht.put(1,"kiwi")
# print(ht.get("apple"))
# ht.remove(5)
# print(ht.get(5))


# class Node:
#     def __init__(self,key,value):
#         self.key = key
#         self.value = value
#         self.next = None
# class HashTable:
#     def __init__(self,size):
#         self.size = size
#         self.table = [None] * size
#     def hashFunction(self,key):
#         return hash(key) % self.size
    
#     def put(self,key,value):
#         index = self.hashFunction(key)
#         if not self.table[index]:
#             self.table[index] = Node(key,value)
#         else:
#             node = self.table[index]
#             while node.next:
#                 if node.key == key:
#                     node.value = value
#                     return
#                 node = node.next
#             node.next = Node(key,value)

#     def get(self,key):
#         index = self.hashFunction(key)
#         node = self.table[index]
#         while node:
#             if node.key == key:
#                 return node.value
#             node = node.next
#         raise KeyError("key not found")
    
#     def remove(self,key):
#         index = self.hashFunction(key)
#         if not self.table[index]:
#             raise KeyError("key not found")
#         if self.table[index].key == key:
#             self.table[index] == self.table[index].next
#             return
#         prev = None
#         curr = self.table[index]
#         while curr:
#             if curr.key == key:
#                 prev.next = curr.next
#                 return
#             prev = curr
#             curr = curr.next
#         raise KeyError("Key not found")