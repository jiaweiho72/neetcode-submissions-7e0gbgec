class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        Q
        - given normal padlock with 4 digits
        - start at '0000'
            - return min no of turns to reach target combination
            - catch: of you hit a deadend, return -1 (invalid)
            - you can turn backwards too

        brainstorm
        - need a way to quickly detect deadend
            if target = 5, will be impossible if deadend <=5 and >=5
        - each digit affects the other. As only if you hit the FULL deadlock, then it's an issue, else ok
        - bruteforce, go through every combination from 0000 to target -> only solution

        graph (like start -> end word)
        - every intermediate transition state is one letter difference. 
        - can go foward or backwards. 
        - BFS so like the shortest path. so the first time it reaches target -> optimal shortest distance 
        
        - use visited set and add deadends
            - visit until no more to visit and you by then should have early returned when found target
        """

        from collections import deque
        
        # BFS: start search from  "0000"
        queue = deque(["0000"])
        visited = set(deadends)
        steps = 0
        no_of_digits = 4

        if "0000" in visited:
            return -1
        if target == "0000":
            return 0


        while queue:
            steps += 1
            level_size = len(queue)
            for _ in range(level_size):
                cur_combination = queue.popleft()
                if cur_combination in visited:
                    continue
                visited.add(cur_combination)
                for i in range(no_of_digits):
                    cur_digit = int(cur_combination[i])
                    for j in [1, -1]: # postitive and negative direction
                        new_digit = (cur_digit + j) % 10
                        next_lock = cur_combination[:i] + str(new_digit) + cur_combination[i + 1:]
                        if next_lock == target:
                            return steps
                        queue.append(next_lock)

        # if reached here -> searched every unblocked path and did not find target
        return -1
                        












