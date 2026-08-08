class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        8 Aug 2026
        - given list of queries, return list of answer
            - answer is whether u is a prereq of v

        idea
        - precompute
            - for each node, have a set of nodes that are prereq
        - kahns algo
            - tabulate and propogate to successor
            - adj_list [prereq -> [courses]]
            - calculate all indegrees and queue
                - start visiting indegrees = 0 (leaf prereqs)
                - visit neighbours
                    - decrement neighbour's indegree
                    - if neighbour indegree == 0 -> enqueue
            two ideas: prereq: {courses depending} or course: {prereqs needed}
            - as you are going from bottom up, it is easier to pass upwards
                - if you go upwards, you are not tracking the parent so hard to update ancestors: courses depending
                - if you go upwards, you can still pass the current as a prereq for the child
            - there is nothing if you try to update current node 
            - but if you update the neighbours with the prereq and it's prereq
        """

        from collections import deque

        # 1) build adj_list
        adj_list = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for prereq, course in prerequisites:
            # prereq -> course
            adj_list[prereq].append(course)
            indegrees[course] += 1

        # Keeping track of each nodes indirect prereqs
        node_to_prereqs = [set() for _ in range(numCourses)] # inside is set()

        # 2) Kahns algo
        queue = deque([node for node, indegree in enumerate(indegrees) if indegree == 0])
        while queue:
            node = queue.popleft()
            neighbours = adj_list[node]
            for neighbour in neighbours:
                node_to_prereqs[neighbour].add(node) # add node as prereq
                #node_to_prereqs[neighbour] = node_to_prereqs[neighbour].union(node_to_prereqs[node]) # add node's prereqs too
                node_to_prereqs[neighbour].update(node_to_prereqs[node])
                indegrees[neighbour] -= 1 # simulate pop cure node
                if indegrees[neighbour] == 0:
                    queue.append(neighbour)

        # 3) Build answers
        answers = []
        for u, v in queries:
            answers.append(
                u in node_to_prereqs[v]
            )
        return answers

        







