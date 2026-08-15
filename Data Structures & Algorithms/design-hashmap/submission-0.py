class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    SIZE = 1000

    def __init__(self):
        self.hashset = [ListNode() for _ in range(self.SIZE)]

    def hash(self, key): # returns index
        return key % self.SIZE

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        node = self.hashset[index]
        while node: # stop when reach end (None)
            if node.key == key: # already inside -> update val
                node.val = value
                return
            if not node.next:
                break
            node = node.next
        node.next = ListNode(key, value) # reach here means just add to the end
        

    def get(self, key: int) -> int:
        index = self.hash(key)
        node = self.hashset[index]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        # reach here means can't find
        return -1
        

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
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)