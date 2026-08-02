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
        
            
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)