class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Area = width * min_height

        Bruteforce - O(n^2)
        - for each starting pt go through window sizes
        Comparing to 'container with most water'
        - instead of just the min of two points, it is now min of all points in between

        Monotonic INCREASING Stack O(n) space and time
        - Stack of (Height, index)
        - Iterate from front
            - cleaning stack if current does not follow increasing trend
                - while cur height < top of stack height
                    - top of stack can't be extended further anymore
                        - calculate the area and check max area
            - add new cur height ele to stack
                - note: the index is the last ele's index in the stack after popping
                    - extending backwards as it can form a valid rectangle as cur height after cleaning is now more than top of stack
        - At the end calculate remainder
            - there will be leftover pairs in the stack
            - calculate their areas from the rightmost end point


        note: monotonic increasing -> if less than then while loop to pop until valid increasing trend
        """
        max_area = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # Monotonic increasing: Clean while not increasing (h < top of stack)
                pop_index, pop_height = stack.pop()
                max_area = max(max_area, pop_height * (i - pop_index))
                start = pop_index
            stack.append((start, h)) # start is the leftmost index where cur can start a valid rectangle of it's height

        # process leftover
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area






