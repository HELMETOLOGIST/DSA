class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self,value):
        if value not in self.queue:
            self.queue.insert(0,value)
            return True
        return False
    
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("Queue is Empty")

    
    def size(self):
        return len(self.queue)
    

TheQueue = Queue()
TheQueue.enqueue("Sinan")
TheQueue.enqueue("Favas")
TheQueue.enqueue("Shibil")
TheQueue.enqueue("Asif")
TheQueue.enqueue("Nibin")
print(TheQueue.size())
print(TheQueue.dequeue())
print(TheQueue.dequeue())
print(TheQueue.dequeue())
print(TheQueue.dequeue())
print(TheQueue.dequeue())
print(TheQueue.dequeue())



class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        srt = "-->".join([str(x) for x in self.items])
        return "%s" % srt
    
    def enqueue(self,x):
        self.items.append(x)
        
    def dequeue(self):
        self.items.pop(0)

def Start():
    q = Queue()
    q.enqueue(4)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(2)
    q.enqueue(9)
    q.dequeue()
    print(q)
Start()
