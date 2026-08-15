class ListNode:
    def __init__(self, key=None):
        self.key = key
        self.next = None

class MyHashSet:
    """
    Hashset NOT hashmap -> no need store value
    - a fixed size list -> linked list for collisions
    - hashing modulo by the size of the list to find the index
        - if conflict, add to the linked list of collisions
        - to serach, need to iterate through every one
    """
    SIZE = 1000

    def __init__(self):
        self.hashset = [ListNode() for _ in range(self.SIZE)]

    def hash(self, key): # returns index
        return key % self.SIZE

    def add(self, key: int) -> None:
        index = self.hash(key)
        node = self.hashset[index]
        while node: # stop when reach end (None)
            if node.key == key: # already inside -> ignore
                return
            if not node.next:
                break
            node = node.next
        node.next = ListNode(key) # reach here means just add to the end

    def remove(self, key: int) -> None:
        index = self.hash(key)
        node = self.hashset[index]
        prev = None
        while node: # stop when reach end (None)
            if node.key == key: # found and remove
                prev.next = node.next
                return
            prev = node
            node = node.next

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        node = self.hashset[index]
        while node:
            if node.key == key:
                return True
            node = node.next
        # reach here means can't find
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)