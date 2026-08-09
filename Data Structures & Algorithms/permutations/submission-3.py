class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        - return list of permutations

        special
        - need permutations of the remaining elements

        instead of using a nums list to keep track of which elements left for used (list slicing is costly)
        - used a visited boolean list to track which has been used
            - for loop just skips this element which is already in the current permutation path

        Time: O(n · n!)
        - n! permutations
        - cur.copy() is n

        Space
        cur → O(n)
        visited → O(n)
        recursion stack → O(n)
        result -> O(n · n!)

        """

        result = []
        n = len(nums)
        visited = [False] * n  # track which numbers are used

        def backtrack(cur):
            if len(cur) == n:
                result.append(cur.copy())
                return

            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = True
                cur.append(nums[i])
                backtrack(cur)

                cur.pop()
                visited[i] = False

        backtrack([])
        return result







        """ 
        BAD example don't use, list slicing adds n
        19 jun 2026
        - return all -> backtracking

        - not just simple choose or don't choose at each step
            - each step you have multiple options to choose at each recursion as you can start from anywhere
        
        Time:
        note O(n^n * n^2)
            - as 
        Space:
        O(n) - recursion stack
        """

        result = []
        cur_list = []
        def backtracking(nums_left): # cur and the list left
            # base case:
            if not nums_left: # empty list
                result.append(cur_list.copy())
                return


            for i in range(len(nums_left)):
                num = nums_left[i]

                # add current num
                cur_list.append(num)
                backtracking(nums_left[:i] + nums_left[i+1:])

                # don't include (permutation you must include all elements, can't skip)
                cur_list.pop()
        
        backtracking(nums)
        return result



        