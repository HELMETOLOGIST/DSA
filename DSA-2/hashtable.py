class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]
     
    def hash_function(self, key):
        return hash(key) % self.size
     
    def set(self, key, value):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
         
    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        index = self.hash_function(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

# Example usage:
ht = HashTable(10)
ht.set("apple", 5)
ht.set("banana", 10)
ht.set("orange", 15)

print(ht.get("apple"))  # Output: 5
print(ht.get("banana"))  # Output: 10

ht.remove("banana")
print(ht.get("banana"))  # Output: None
