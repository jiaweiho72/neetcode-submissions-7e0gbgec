class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Build entire adj_set is costly and not recommended

        Question
        - return no of words in shortest transformation from start to end word
            - every inbetween node differ by one character and they must be in word dict

        Idea - Graph as there are existing state nodes and not you making decisions to create these states
        - convert word list to word set for O(1) lookup
        - BFS from begin word
            - start couting distance(level) from 0
            - iterate by level
            - generate all possible words changing one character a time
                - if generated in word_set, add to queue to continue searching
                - must remove from word set to signify visited (visited set works too)
                    1) this prevents you from infinite loop 'hit' -> 'hot' -> 'hit' cycle
                    2) this reduces unnecessary repeated work for already visited work
                        - the answer would still be correct without it
                            as even if you visit, the shorter path would have reached before and return
                        - say your shortest path reaches x already, then a longer path reaches x
                            - if not marked visited, it will do the full search loops again at x
                            - but this is not needed as you already found the shortest path in the first hit
                - you may think: what if path1 is the longer path and it visits x and mark as visited, then
                path2 comes to x and is already visited so does not consider?
                    - but this is BFS level-by-level iteration. which means the first path that reached
                    x is guaranteed the shortest path already. 

            - return distance when end_word is found


        Time: O(N * L^2)
        N = number of words in wordList
        L = length of each word
        - BFS every node only once (help with visited set) O(N)
            - as only visit if in the word set
            - in one bfs of a word
                try every index of the word O(L)
                    try every possible 26 characters
                    but string slicing is O(L)
                O(26L^2)

        Space: O(N)
        - word_set O(N)
        - queue O(N)
        - ignore L if treat each string as a single object and not counted, else O(N*L)
        """


        word_set = set(wordList) # O(N)
        result = 0

        queue = deque([beginWord])
        while queue:
            result += 1 # increment distance

            # iterate level
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node == endWord: # reached the end (first time is optimal as unweighted BFS)
                    return result

                for i in range(len(node)):
                    for c in range(ord('a'), ord('z') + 1):
                        char = chr(c)
                        if char == node[i]: # alr this char, no need to try swap
                            continue
                        candidate_neighbour = node[:i] + char + node[i + 1:]

                        if candidate_neighbour in word_set: # valid path
                            queue.append(candidate_neighbour)
                            word_set.remove(candidate_neighbour) # remove 

        # reach here means did not find valid sequence
        return 0




