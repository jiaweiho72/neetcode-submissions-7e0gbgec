class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        - Increment from the back
        - keep track of the carry over to add (if sum >= 10)
        - Note may need to add a new element at the front O(n)

        Time complexity: O(2n)
        Space complexity: O(1)
        """
        n = len(digits)
        carry_over = 1
        for i in range(n - 1, -1, -1):
            digit = digits[i]
            digit_sum = digit + carry_over
            carry_over = 0
            if digit_sum >= 10:
                carry_over = digit_sum // 10 # First digit
                digit_sum = digit_sum % 10 # Second digit
            digits[i] = digit_sum
            if carry_over == 0:
                break
        
        # Handle the case where there is still carry_over and have to add one more element
        if carry_over:
            digits = [carry_over] + digits # O(n)
        return digits