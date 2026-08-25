class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        25 Aug 2026
        question
        - opp collide and smaller explodes
            - same size -> both explodes
        - same direction never collides
        - the survivor of the collision continues headon
        - survivors(may be no collision) remain in the list for future collisions
            - those exploded in between disappear

        [2,4,-4,-1]
        2,4 no collision but may still collide in future
        4,-4 both explode
        2,-1 collision


        Stack
        - iterate in order and save previous elements for processing
        - reporcess them it is in order of iteration from the latest first

        left can bash through all the way to the right
        same, right can bash trhough all the way to the left

        iterate from the left to right to clear but you need to clear the stack backwards as long as it can
        mistake: direction matters too left or right\
            - will only collide if left is moving -> and right is moving <-

            - right is moving ->, does not matter if left is <- or ->, it will not collide
            - asteroid != 0
        """

        n = len(asteroids)
        stack = []
        for i in range(n):
            cur = asteroids[i]
            if cur > 1: # will not collide
                stack.append(cur)
            else: # cur < 1
                to_append_cur = True
                while stack and stack[-1] > 0:
                    if abs(stack[-1]) < abs(cur): # smaller stack top explodes
                        stack.pop()
                    elif abs(stack[-1]) > abs(cur):
                        to_append_cur = False
                        break # don't add to stack
                    else: # means both equal -> both explode
                        to_append_cur = False
                        stack.pop()
                        break

                # stack empty or no collision with the next element on top of stack -> either way add current
                if to_append_cur:
                    stack.append(cur)
        
        return stack









