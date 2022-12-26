# LRU记住两件事 双向链表+hashmap存储
# 增 删 移动到头 删除尾
# 这样就能快速做出来

class DLinkNode:
    def __init__(self, key=0, value=0):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:
    
    def _add_node(self,node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _move_to_head(self,node):
        self._remove_node(node)
        self._add_node(node)
        
    def _pop_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node
        
    def __init__(self, capacity: int):
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.dict = {}
        self.length = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        node = self.dict.get(key,None)
        if not node:
            return -1
        else:
            self._move_to_head(node)
            return node.value
        

    def put(self, key: int, value: int) -> None:
        node = self.dict.get(key,None)
        if not node:
            node = DLinkNode()
            node.key=key
            node.value = value
            
            self._add_node(node)
            self.dict[key] = node
            self.length+=1 
            
            if self.length>self.capacity:
                tail = self._pop_tail()
                del self.dict[tail.key]
                self.length-=1
        else:
            node.value = value
            self._move_to_head(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)