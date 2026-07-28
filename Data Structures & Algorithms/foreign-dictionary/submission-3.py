class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        28 July 2026
        
        doubts
        - inside each word sorted? No

        problem
        - return string of unique letters in sorted order
            multiple solutions, return any
        - if invalid (cycle) -> return ""
        - ordering
            a < b if 'abcd' vs 'abxd' (first letter differ)
            a < b if 'abc' vs 'abcee' (length)
        * only need to compare the first differing letter
            - because if you compare the next, the comparison is not balanced alr as the char before isn't the same


        idea
        - collate a graph (adj_dict) of edges
        - go through every word
            compare it and the prev word
            - for each char, find the first differing characters
                - add an edge to the adj_dict
            - if one out of bounds (shorter word) and still same char
                - ignore

        toposort the adj_dict
        important
        - init the graph first cause there are edge cases like
            words = ["abc", "abc"] should return "abc" not ""
        - need invalid prefix check 
            ["abc", "ab"] is impossible
        - use set in adj_dict as there may be duplicate so you need quick check if
            current edge already in adj_dict


        Time: let n be no of characters
        - init adj_dict/indegrees list O(n)
        - build graph O(n)
        - kahn's algo
            V - visit every node (n)
            E - for each node, there is forloop for neighbours E1 + E2 + Ei ... = E
                - you visit every vertex once and every edge once
                - every vertex is queue and processed once
                - every edge is visited through the neighbour for loop, even if ended up not enqueued or is alr visited. 
                    the act of checking is a computation
        O(V + E)

        Space:
        - O(n)
        """
        from collections import defaultdict, deque

        n = len(words)

        # Init every char in word list
        adj_dict = {}
        indegrees = {}
        for word in words:
            for char in word:
                adj_dict[char] = set()
                indegrees[char] = 0
        

        # 1) Build adj graph
        for i in range(1, n):
            prev_word, cur_word = words[i - 1], words[i]
            # invalid prefix check example ["abc", "ab"]
            if len(prev_word) > len(cur_word) and prev_word.startswith(cur_word):
                return ""
            min_size = min(len(prev_word), len(cur_word)) # to prevent OOR

            for j in range(min_size):
                prev_char, cur_char = prev_word[j], cur_word[j]
                if prev_char != cur_char:
                    if cur_char not in adj_dict[prev_char]: # new edge
                        adj_dict[prev_char].add(cur_char) # prev -> cur
                        indegrees[cur_char] += 1 # inbound 1 to char
                    break

                # else they are all the same

        # 2) Topo sort the letters (kahn's algo)        
        V = len(adj_dict)
        queue = deque()
        # insert chars with indegree == 0 inside
        for char, indegree in indegrees.items():
            if indegree == 0:
                queue.append(char)

        result_str = ""
        while queue:
            cur_char = queue.popleft()
            result_str += cur_char
            
            neighbours = adj_dict[cur_char]
            for neighbour in neighbours:
                # simulate pop current parent
                indegrees[neighbour] -= 1

                if indegrees[neighbour] == 0:
                    queue.append(neighbour)

        return result_str if len(result_str) == V else ""

            

        










