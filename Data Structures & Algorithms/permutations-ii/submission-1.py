class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        20 sep 2026
        - return permutations. has duplicates

        idea
        - permutations need all elements and order matters
        - go one by one the output index
            - each time try all possible remaining values
                - not like combination where you select i and the remaining is i+1->n
                    - this works cause order does not matter and selecting i now, you can ignore the case
                    of i and element before i eg. if at 2, don't neeed to check one for the 2,1 case
                    - because element before i would check itself and i case. eg at 1 it checks 2 case so 1,2 case handled
                - because this is permuation where 1,2 and 2,1 is diff, need to still go backwards
                    - but since now your search space is everything, there may be conflicts
                        - because in diff iterations every same element is in the search space, so
                        you may be choosing duplicate elements which is wrong

                - thus, need to keep track of a remaning elements left. (it would not be in order)
        - handle duplicate by skipping same values. Need to sort nums first

        - duplicate
            - same level handling of the removal eg. making [1] and [1] again
            - if multi level duplicates, will not skip eg. making [1,1,2]

                    [1,1,2]
                    1     2
            1,1 1,2         2,1
        1,1,2     1,2,1         2,1,1


        mistake: removing and appending from list destroy's remaining list sorted order
        - solution
            - can't use sets too as there are duplicates so you can't insert properly
            - use a boolean list

        """


        nums.sort()
        n = len(nums)
        result = []

        def dfs(cur, bool_list): # i index of output; returns nothing
            # 1) base case
            if len(cur) == n: #  done with forming the permutation
                result.append(cur.copy())
                return
            
            for j in range(n):
                # skip invalid case
                if bool_list[j]:
                    continue
                """
                because now j is not the list of possible candidates. it is the list of everything
                - so when looking for duplicate, since you are looking at the whole list, need to adjust
                eg. 1,1,2
                - you used 1 previously then you can still use it in the next level
                - then when you are at the next index
                    - the previous 1 is still in the value space, as value space is the whole list
                    - you should not skip this new one if the previous was used
                - if the previous 1 was unused in the same iteration level -> skip it
                
                time: n! * n 
                space n! * n
                """
                if (j != 0 and nums[j - 1] == nums[j]) and not bool_list[j - 1]: # while duplicate with previous element
                    continue

                candidate = nums[j]
                bool_list[j] = True # use the jth element
                cur.append(candidate)
                dfs(cur, bool_list)

                bool_list[j] = False
                cur.pop() # pop the most recently added candidate - will it be correct?


        dfs([], [False] * n)
        return result
            







