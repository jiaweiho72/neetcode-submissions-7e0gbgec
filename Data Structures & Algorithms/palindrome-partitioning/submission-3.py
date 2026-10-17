class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        17 Oct 2026
        try every combindation and check if palindrome. not permutatino as it is substring in order

        build palindrome at start index 
        - after every one built, add to path and update new start

        mistakes 
        - did not return after copying 
        - next new palindrome should start from end + 1
        """

        def is_palindrome(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        n = len(s)
        result = []

        def dfs(start, path):
            if start == n: # OOB - reach here is valid
                result.append(path.copy())
                return
        
            for end in range(start, n): # start as single letter is a palindrome
                if not is_palindrome(start, end):
                    continue
                path.append(s[start:end + 1])
                dfs(end + 1, path)
                path.pop()
                
        dfs(0, [])
        return result
        

















        """
        10 Aug 2026
        - split s into palindrome substings
        - return all possible lists

        Idea backtracking
        - try letter and add if it is a valid palindrome
        - palidrome checker helper function

        dfs(i, cur_str): # index of s
            # base case


            for j in range(i, n):
                check if cur_str+s[j] is a palindrome
        """

        n = len(s)
        def is_palindrome(start, end):
            l, r = start, end
            while l < r: # odd case == does not matter as it is the same element -> confirm equal
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        result = []
        def dfs(start, cur_path):
            if start == n: # out of bounds -> used all elements -> valid
                result.append(cur_path.copy())

            for end in range(start, n):
                """
                the options are not elements from i to n
                the option is current string choice of s[i:j+1], s[i:j+2] ....
                """
                if not is_palindrome(start, end):
                    continue
                
                cur_path.append(s[start:end + 1])
                dfs(end + 1, cur_path)
                cur_path.pop()
        dfs(0, [])
        return result










