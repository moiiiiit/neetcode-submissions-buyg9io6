class Node():
    def __init__(self, value, key, prev, next):
        self.value = value
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache = {}
    
    def add_to_front(self, new_head):
        if not self.head:
            self.head = new_head
            self.tail = new_head
            return
        old_head = self.head
        old_head.prev = new_head
        new_head.next = old_head
        self.head = new_head
    
    def remove_from_end(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        old_tail = self.tail
        new_tail = old_tail.prev
        new_tail.next = None
        self.tail = new_tail
    
    def remove_doubly_connected_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def move_to_front(self, node):
        if node == self.head:
            return
        if node == self.tail:
            backup_node = node
            self.remove_from_end()
            self.add_to_front(node)
            return
        self.remove_doubly_connected_node(node)
        self.add_to_front(node)

    
    def get(self, key):
        if key in self.cache:
            self.move_to_front(self.cache[key])
            print(self.cache)
            return self.cache[key].value
        else:
            return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.cache[key].value = value
            self.move_to_front(self.cache[key])
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.tail.key]
                self.remove_from_end()
            new_node = Node(value, key, None, None)
            self.cache[key] = new_node
            self.add_to_front(new_node)
