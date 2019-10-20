class LinkedNode:
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
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
        self.kick(self.key_to_prev[key])
        return self.key_to_prev[key].next.value
    
    
# prev---node---next-------tail
# prev---next-------tail---node
    def kick(self, prev):
        node = prev.next
        if node is self.tail:
            return 
        prev.next = node.next
        if node.next:
            self.key_to_prev[node.next.key] = prev
            node.next = None
        self.push_back(node)
        
    def push_back(self, node):
        self.tail.next = node
        self.key_to_prev[node.key] = self.tail
        self.tail = node
        
    def pop_front(self):
        head = self.dummy.next
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy
        del self.key_to_prev[head.key]
        
    
    def put(self, key: int, value: int) -> None:
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.key_to_prev) > self.capacity:
                self.pop_front()
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
