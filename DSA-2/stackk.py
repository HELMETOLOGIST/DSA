class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "-->"
            cur = cur.next
        return out
    
    def push(self,value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def pop(self):
        if self.isEmpty():
            raise Exception("It is a Empty Stack")
        
        current = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return current.value
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from and Empty Stack")
        return self.head.next.value
    

    def getSize(self):
        return self.size
    

stack = Stack() 
stack.push(34)
stack.push(12)
stack.push(52)
stack.push(87)
stack.push(45)
stack.push(23)

print(f"Stack: {stack}")

stack.pop()
stack.pop()
print(f"Poping: {stack}")