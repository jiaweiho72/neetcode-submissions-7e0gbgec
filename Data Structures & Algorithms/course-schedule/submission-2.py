class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        4 Sep 2016
        - given prereqs, numCourses, return true if can finish all courses
        - courses labeled from 0 to numCourses - 1

        traverse but need to complete all prereq then can move on to the next
        - Khans
            - calculate indegrees
            - BFS starting from nodes with indegrees. Push to queue when indegree decrement to 0
                - cause indegree 0 means no incoming nodes that have not been completed -> can process
            - if no of iterations processed less than numCourses, means early return and not all visited
            what about cycle?
        - since graph is 0 to numCourses-1: can use a list instead of a dictionary mapping key mapping for adjlist
        
        mistake: no need check for visited for cycle? 
        - cause if there is a cycle
            - the nodes in the cycle will forever have at least one incoming degree and will never
            be processed. Cus you only process nodes that have 0 indegree and finishing one node, you relax
            your neighbours. But in cycle it is impossible to remove any edge in the cycle to give one
            node an indegree 0 cause the child is also in the cycle and has child that can't be relaxed ...
        - thus the number of nodes processed in the end is not all the nodes and processed_count == numCourses checks this
        
        
        
        Time: O(V+E) + E for processing
        - BFS V main loop
            - inside it visits all neighbours: n1 + n2 + ... + nV = E

        Space: O(V + E)
        - adj_list = O(V + E)
            - V nodes
            - no of items in the sub list in FULL total = E
        - queue = O(V)
        
        25 mins
        """
        from collections import deque

        # 1) Build adj_list and get indegrees
        adj_list = [[] for _ in range(numCourses)] # list of list
        indegrees = [0] * numCourses # index is the course

        for course, prereq in prerequisites:
            # prereq -> course
            adj_list[prereq].append(course)
            indegrees[course] += 1

        # 2) init BFS queue with indegrees 0
        initial_nodes = [node for node, indegree_count in enumerate(indegrees) if indegree_count == 0]
        queue = deque(initial_nodes)

        # 3) Kahns algo
        processed_count = 0
        while queue:
            cur = queue.popleft()
            processed_count += 1
            
            # visit neighbours
            neighbours = adj_list[cur]
            for neighbour in neighbours:
                indegrees[neighbour] -= 1 # decrement neighbours cur points to
                if indegrees[neighbour] == 0: # if neighbour has no prereqs left -> queue to process queue
                    queue.append(neighbour)

        return processed_count == numCourses
        













        """
        28 July 2026
        - return true if can finish all courses.

        doubts
        - courses zero-indexed

        topo sort - kahn algo
        - indegrees count
        - queue nodes with indegree == 0
        - while queue

        if can finish all courses, all nodes should be visited in kahn
    
        """
        from collections import deque

        adj_list = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        # 1) Init graph
        for course, prereq in prerequisites:
            # prereq -> course
            adj_list[prereq].append(course)
            indegrees[course] += 1

        # 2) Kahn's algo
        # populate current indegree == 0 nodes
        queue = deque([node for node, indegree in enumerate(indegrees) if indegree == 0])
        processed_count = 0
        while queue:
            cur_node = queue.popleft()
            neighbours = adj_list[cur_node]
            for neighbour in neighbours:
                # simulate pop cur node as it is DONE = can be reached
                indegrees[neighbour] -= 1

                # if all parents can be reached, this child can also be completed
                if indegrees[neighbour] == 0:
                    queue.append(neighbour)

            processed_count += 1

        return numCourses == processed_count