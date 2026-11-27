class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    """
    diff: wildcard letters
    - with this, you should try every children

    at .
    - for each of the children, need its own branch of search
        - sub problem dfs
        - recursively try -> propogate for each element in level, do its own search, call recursive search
            - do the same thing multiple times, but no fixed for loop
    """
    def __init__(self):
        self.dummy = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur_node = self.dummy
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = TrieNode()
            cur_node = cur_node.children[c]
        cur_node.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        cur_node = self.dummy
        n = len(word)
        def dfs(i, cur_node):
            for j in range(i, n):
                c = word[j]
                if c == ".":
                    for child, child_node in cur_node.children.items():
                        if dfs(j + 1, child_node): # just need one valid path
                            return True
                    return False
                else:
                    if c not in cur_node.children:
                        return False
                    cur_node = cur_node.children[c]
            return cur_node.is_end_of_word
                    
        return dfs(0, cur_node)









'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:
    """
    Addword
    - time: O(len(word))
    - space: O(len(word))

    search
    - time: depends of no of '.' wildcards
        - if no '.' O(n) pass through len of word n
        - worst case all '.'
            O(n · 26^k)
            - 26 alphabet children choices at each dfs -> 26 ^ k
                k dots
                so 26 ^ k paths
            - each of the 26 ^ k paths would check up to n characters of the search word
                - the inner for loop
            so basically 26^k dfs search path calls and inside each there is a for loop with max n
    """

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode() # Only if does not exist, then you can add
            cur = cur.children[char]
        cur.end_of_word = True # Mark the end of the word
            

    def search(self, word: str) -> bool:
        def dfs(j, cur): # DFS from j onwards
            for i in range(j, len(word)):
                char = word[i]
                if char == ".":
                    for child in cur.children.values(): # Dictionary of nodes
                        # return dfs(i + 1, child) # Wrong as this returns the very first exploration even when false, thus returning false
                        # This returns true only when it is found
                        if dfs(i + 1, child):  
                            return True
                    return False # Could not find anything after all the DFS
                else: # Normal search
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
            return cur.end_of_word
        return dfs(0, self.root)
'''
            
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)