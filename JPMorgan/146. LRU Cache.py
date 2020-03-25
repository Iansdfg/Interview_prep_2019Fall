class LinkedNode:
    def __init__(self, val = None, key = None, next = None):
        self.val = val
        self.key = key
        self.next = next
        
class LRUCache:

    def __init__(self, capacity: int):
        self.key_to_prev = dict()
        self.capacity = capacity
        self.dummy = LinkedNode()
        self.tail = self.dummy
        
    def get(self, key: int) -> int:
        if key not in self.key_to_prev:
            return -1
        res = self.key_to_prev[key].next.val
        self.kick(self.key_to_prev[key])
        return res
        
    def put(self, key: int, value: int) -> None:
        if key in self.key_to_prev:
            self.key_to_prev[key].next.val = value
            self.kick(self.key_to_prev[key])
        else:
            new = LinkedNode(value, key, None)
            self.append(new)
            if len(self.key_to_prev) > self.capacity:
                self.pop_front()
                
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
        
    def pop_front(self, ):
        head = self.dummy.next
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy
        del self.key_to_prev[head.key]
        
        
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
