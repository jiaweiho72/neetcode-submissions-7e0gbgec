class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        1 Jul 2026
        - input: speed and position of ith car
        - car fleet (cars driving beside each other) -> speed is min speed of these cars
        - return no of car fleets

        Idea
        - position towards the end should be checked first as they will be the leaders of fleets and cars on the left of array will get stuck to it. They have higher piority
        - idea: count by checking each car from its position if it will join the fleet, else it will form a new fleet
            - a way to compare is the time taken to reach target
                - because both speed and position matters
        - use a stack to keep track of the fleet (same as array)

        mistake:
        - the list is not sorted by position
        """

        stack = []
        combined = list(zip(position, speed))
        combined.sort()
        n = len(combined)
        for i in range(n - 1, -1, -1):
            p, s = combined[i]
            time_taken = (target - p) / s
            last_time = stack[-1] if stack else -1
            if time_taken > last_time: # It is slower than the last fleet
                stack.append(time_taken)
            else: # It is same or faster and will join this fleet
                continue # no need to add new fleet
            
        return len(stack)
        
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

        16 mins
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





