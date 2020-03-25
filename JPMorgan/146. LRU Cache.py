class LinkedNode:
    def __init__(self, val = None, next = None, key = None):
        self.val = val
        self.next = next
        self.key = key
        
class LRUCache:
    def __init__(self, capacity: int):
        self.key_to_prev = dict()
        self.capacity = capacity
        self.dummy = LinkedNode()
        self.tail = self.dummy

    def get(self, key: int) -> int:
        if key not in self.key_to_prev:
            return -1 
        self.kick(self.key_to_prev[key])
        return self.key_to_prev[key].next.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.val = value
        else:
            self.append(LinkedNode(value, None ,key))
            if len(self.key_to_prev) > self.capacity:
                self.pop_fornt()
        
    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return 
        
        nextt = node.next 
        prev.next = nextt
        if nextt:
            self.key_to_prev[nextt.key] = prev
        self.append(node)
        
    def append(self, node):
        self.tail.next = node
        self.key_to_prev[node.key] = self.tail
        self.tail = node
        
    def pop_fornt(self, ):
        head = self.dummy.next 
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy
        del self.key_to_prev[head.key]
        
        
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
