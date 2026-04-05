
class ListNode:
    def __init__(self, key=None, val = None, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    """
    requirements
    - init cache capacity
    - get value of key if exists, else -1
        - get will make it recently used
    - put key:value and update if key exists.
        - if exceeds capcity, remove LRU
    - O(1)

    idea
    - dict for key value O(1) retrieval
        value will be the list node
    - doubly linkedlist to keep track of LRU
        - left and right pointers
            - for removing and adding

    get
    - get value from dict
    - remove from linked list and append to the right most recently used
        - helper functions -> remove from any index + insert at most recent

    put
    - if exits in dict
        - remove from linkedlist
    - either ways we will add to the most recent in the linked list 
    - check after if exceeeds capacity -> if it does, remove the leftmost node

    mistakes
    - node need to store key too for eviction part where you remove the node.
    but need the key to remove from cache too
    """


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = ListNode()
        self.right = ListNode()

        self.left.next = self.right
        self.right.prev = self.left
    
    # Helper functions - insert key and remove key
    def insert(self, node : ListNode):
        # insert to the right end of the linkedlist
        right_node = self.right.prev

        right_node.next = node
        node.prev = right_node

        self.right.prev = node
        node.next = self.right

    def remove(self, node: ListNode):
        # remove from anywhere
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        # get value
        if key not in self.cache:
            return -1 # no need to update linkedlist
        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node) # delete old value. new one will overwrite
        new_node = ListNode(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        # check capacity
        if len(self.cache) > self.capacity:
            lru_element = self.left.next
            self.remove(lru_element) # remove leftmost element
            self.cache.pop(lru_element.key)



