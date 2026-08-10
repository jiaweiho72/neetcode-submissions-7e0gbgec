class Solution:
    def isHappy(self, n: int) -> bool:
        # In python dividing and integer always does not round 
        # up or down but it just ignores the decimal

        # Visited set to check for cycles
        visited = set()
        cur = n

        while cur not in visited: # if equals, it is a cycle
            print(cur)
            visited.add(cur)
            sum_of_squares = 0
            while cur > 0:
                digit = cur % 10 # Last digit
                cur = cur // 10
                sum_of_squares += digit ** 2
            if sum_of_squares == 1:
                return True
            cur = sum_of_squares
        return False