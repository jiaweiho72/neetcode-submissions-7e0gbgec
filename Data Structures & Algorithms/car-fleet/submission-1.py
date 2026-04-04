class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        4 Apr 2026
        - car fleet -> same position at same speed
        - return no of different car fleets

        - logic: if you are position behind but you will reach the destination earlier than the one infront
            -> you will join it's fleet
            - it's not important how fast as you may be faster than infront but may not catchup by the time reach destination

        solution
        - zip(position, speed)
        - sort by position

        - start from the position closest to the destination
            - cus we need to see what are blocking as th right side will block and define the fleets
            - monotonic stack
                - element in stack is a unique fleet
                - compare time to reach destination
                    - if cur time to reach is more than the top of stack, it will be it's own fleet
                    - equals will also stuck to the fleet

        core idea: using destination ETA to compare if will be stuck to a fleet
        """

        combined = list(zip(position, speed))
        n = len(combined)
        combined.sort()
        stack = []

        for i in range(n - 1, -1, -1):
            cur_pos, cur_speed = combined[i]
            reach_time = (target - cur_pos) / cur_speed

            if not stack:
                stack.append(reach_time)
            elif reach_time > stack[-1]:
                stack.append(reach_time)
            
        return len(stack)





