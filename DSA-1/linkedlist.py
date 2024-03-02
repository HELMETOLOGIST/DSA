class Node:
    """
    A class representing a node in a linked list.
    Each node has a data value and a reference to the next node in the list.
    """
    def __init__(self,data):
        """
        Initializes a new node with the given data value.
        The next reference is set to None.
        """
        self.data = data
        self.next = None

class LinkedList:
    """
    A class representing a linked list.
    The linked list consists of nodes where each node has a data value and a reference to the next node in the list.
    """
    def __init__(self):
        """
        Initializes an empty linked list.
        The head reference is set to None.
        """
        self.head = None

    def PrintLL(self):
        """
        Prints the linked list by traversing it from the head to the end.
        """
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, end="-->")
                n = n.next

    def add_begin(self,data):
        """
        Adds a new node at the beginning of the linked list with the given data value.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self,data):
        """
        Adds a new node at the end of the linked list with the given data value.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next:
            n = n.next
        n.next = new_node

    def add_after(self,target,data):
        """
        Adds a new node after the first occurrence of the target data value in the linked list with the given data value.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n:
            if n.data == target:
                new_node.next = n.next
                n.next = new_node
                return
            n = n.next

    def add_before(self,target,data):
        """
        Adds a new node before the first occurrence of the target data value in the linked list with the given data value.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n and n.next:
            if n.next.data == target:
                new_node.next = n.next
                n.next = new_node
                return
            n = n.next

    def delete_by_value(self,data):
        """
        Deletes the first occurrence of the given data value in the linked list.
        """
        curr_node = self.head
        prev_node = None
        
        while curr_node:
            if curr_node.data == data:
                prev_node.next = curr_node.next
                curr_node = None
                return
            prev_node = curr_node
            curr_node = curr_node.next
            
    def delete_end(self):
        """
        Delete the last node in the linked list.
        """
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        
        curr_node = self.head
        while curr_node.next.next:
            curr_node = curr_node.next
            
        curr_node.next = None

            
    def remove_duplicates_by_value(self,target):
        """
        Remove  all occurrences of a duplicate element from the linked list.
        """
        curr_node = self.head
        prev_node = None
        if self.head is None or target is None:
            return
        
        while curr_node:
            if curr_node.data == target:
                if prev_node is None:
                    self.head = curr_node.next
                else:
                    prev_node.next = curr_node.next
            else:
                prev_node = curr_node
            curr_node = curr_node.next
            
    def remove_duplicates(self):
        """
        Remove duplicates 
        """
        if self.head is None:
            return
        curr_node = self.head
        while curr_node:
            remov = curr_node
            while remov.next:
                if remov.next.data == curr_node.data:
                    remov.next = remov.next.next
                else:
                    remov = remov.next
                curr_node = curr_node.next


    def find_middle_node(self):
        """
        find the middle node of the linked list.
        """
        if self.head is None:
            return
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
    
    def array_to_linkedlist(self,arr):
        """
        Array to LinkedList
        """
        linkedlist = LinkedList()
        for i in arr:
            linkedlist.add_end(i)
        return linkedlist.PrintLL
    
    
    def add_by_index(self, index, data):
        """
        Add the Node by index
        """
        if index < 0:
            print("Index out of range")
            return

        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        prev_node = None
        curr_node = self.head
        count = 0
        while curr_node and count != index:
            prev_node = curr_node
            curr_node = curr_node.next
            count += 1

        if not curr_node and count != index:
            print("Index out of range")
            return

        prev_node.next = new_node
        new_node.next = curr_node
        
    def delete_by_index(self, index):
        """
        Delete Node by index.
        """
        if index < 0:
            print("Index out of range")
            return

        if index == 0:
            self.head = self.head.next
            return

        prev_node = None
        curr_node = self.head
        count = 0

        while curr_node and count != index:
            prev_node = curr_node
            curr_node = curr_node.next
            count += 1

        if not curr_node:
            print("Index out of range")
            return

        prev_node.next = curr_node.next
        
    

li = LinkedList()
li.add_end(10)
li.add_end(20)
li.add_end(30)
li.add_end(40)
li.add_end(50)
li.add_end(60)
li.add_end(70)
li.add_by_index(1, 99)
li.delete_by_index(2)
arr = [3, 4, 76, 8, 9, 12]
link = li.array_to_linkedlist(arr)
middle = li.find_middle_node()
print("Middle Node:",middle)
li.remove_duplicates()

li.remove_duplicates_by_value(70)
li.delete_end()

li.delete_by_value(10)
li.delete_by_value(20)
li.delete_by_value(30)

li.add_before(30,59)

li.PrintLL()