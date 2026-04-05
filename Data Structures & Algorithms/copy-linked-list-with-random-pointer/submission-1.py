"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        5 apr 2026
        - each node has an additional random pointer
        - create deep copy of this list

        - since random nodes, it is hard to deep copy
            - when you try to create a random link but the node is not added yet

        solution
        - make a one to one mapping for old node to a new node. No links yet
        - traverse through the old graph and start mapping the links then for the new LL
        """

        
        # 1) Create node mapping
        mapping = {}
        cur = head
        while cur:
            mapping[cur] = Node(cur.val)
            cur = cur.next
        
        # 2) Form node links
        cur = head
        while cur:
            old_node = cur # can't be none due to while loop condition
            new_node = mapping[cur]

            new_node.next = mapping[old_node.next] if old_node.next else None
            new_node.random = mapping[old_node.random] if old_node.random else None

            cur = cur.next

        return mapping[head] if head else None











