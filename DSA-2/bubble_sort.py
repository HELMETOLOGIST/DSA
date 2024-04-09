def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
arr = [45,39,87,45,33,74]
bubble_sort(arr)
print(arr)

def bubble_sort_sl(arr):
    for i in range(2):
        for j in range(0, i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [7,65,42,34,59,8,5]
bubble_sort(arr)
print(arr[-2])

def bubble_sorted_or_not(arr):
    n = len(arr)
    for i in range(n):
        flag = 0
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0:
            break

arr = [1,2,3,4,53,6,7,8,9]
bubble_sorted_or_not(arr)
print(arr)


# Bubble sort in linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print()

    def bubble_sort(self):
        if self.head is None:
            return
        else:
            swapped = True
            while swapped:
                swapped = False
                current = self.head
                prev = None
                while current and current.next:
                    if current.data > current.next.data:
                        if prev:
                            prev.next, current.next.next, current.next = current.next, prev.next, current.next.next
                            swapped = True
                        else:
                            self.head, current.next.next, current.next = current.next, self.head, current.next.next
                    prev, current = current, current.next
                    
llist = LinkedList()
arr = [45, 39, 87, 45, 33, 74]
for num in arr:
    llist.append(num)

print("Original Linked List:")
llist.display()

llist.bubble_sort()

print("Sorted Linked List:")
llist.display()

# Complexity : - O(n ^ 2)