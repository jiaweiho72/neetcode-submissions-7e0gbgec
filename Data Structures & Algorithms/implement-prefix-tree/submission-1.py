"""
28 Nov 2026
- data structure
    - node and the children. can have unlimited children (set of children)
        - store the value too

insert
- see if word found in path
    - else first diff, iteratively build the path

iteration is one level lagging
"""
class TrieNode:
    def __init__(self):
        self.children = {} # set for fast check for x in dict. val->node
        self.is_end_of_word = False # to determine if a word ended here before

class PrefixTree:

    def __init__(self):
        self.dummy = TrieNode()

    def insert(self, word: str) -> None:
        cur_node = self.dummy
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = TrieNode()
            cur_node = cur_node.children[c] # above step guaranteed to have (added if missing)
        cur_node.is_end_of_word = True


    def search(self, word: str) -> bool:
        cur_node = self.dummy
        for c in word:
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c] # cur node mapped with the current character
        return cur_node.is_end_of_word
        
    def startsWith(self, prefix: str) -> bool:
        cur_node = self.dummy
        for c in prefix:
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c]
        return True
        
        





'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PrefixTree:
    """
    Searching item in dict is O(1), list is O(n) or log(n)
    However, startsWith is inefficient so use Trie
    """
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children: # Add children
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
            

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


'''