class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        9 sept 2026
        - return ordering
        - may be multiple valid answers
        - if not possible, return empty array

        topo sort - kahns algo
        1) init the prereq -> course mapping and the indegree count. 
        2) BFS. Fill the queue with those indegree count == 0
            - 0 means no incoming -> all prereqs 'met'
        3) Main BFS
            - each pop from queue is a valid course so process it
            - visit neighbours and remove cur valid course pointer to it
            - if the decrement in indegree of neighbours, makes it 0 -> add to queue
        
        idea: If there is a cycle -> the elements in the cycle won't be populated in the
        queue -> never processed -> so the queue ends early without every processing the cycle elements
        thus: the final no of processed must be == to the no of nodes


        numCourses from 0 to n-1 so just let the course be the index


        you may think there may be a case where a node indegree becomes zero but then later
        on there may be another relaxed node that will decrease this indegree
        - impossible as this relaxed node, was always in the indegree, so impossible for previous
        indegree to be 0 when this node is still attached
        """
        from collections import deque

        adj_list = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        # 1) Init
        for course, prereq in prerequisites:
            # prereq -> course
            adj_list[prereq].append(course)
            indegrees[course] += 1

        initial_nodes = [node for node, indegree in enumerate(indegrees) if indegree == 0]

        # 2) BFS kahns
        queue = deque(initial_nodes)
        result = []

        while queue:
            cur = queue.popleft()
            result.append(cur)
            neighbours = adj_list[cur]
            for neighbour in neighbours:
                # simulate removing cur from neighbour
                indegrees[neighbour] -= 1
                if indegrees[neighbour] == 0:
                    queue.append(neighbour)
            
        # if got cycle -> invalid -> return empty
        return result if len(result) == numCourses else [] 
        












        """
        28 July 2026
        - diff between I and II, instead of returning boolean if valid, reurn the topo order
            - there are multiple answers, return any
            - return empty array if impossible to finish all courses
        """

        from collections import deque

        # 1) init graph
        adj_list = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for course, prereq in prerequisites:
            # prereq -> course
            adj_list[prereq].append(course)
            indegrees[course] += 1
        
        # 2) Kahn's algo
        # init queue of all nodes where starting indegree == 0
        queue = deque([node for node, indegree in enumerate(indegrees) if indegree == 0])
        topo_order = []

        while queue:
            cur_node = queue.popleft()
            topo_order.append(cur_node)
            neighbours = adj_list[cur_node]

            for neighbour in neighbours:
                # current node can be completed, so remove this degree
                indegrees[neighbour] -= 1

                if indegrees[neighbour] == 0: # all prereq completed
                    queue.append(neighbour)
        
        return topo_order if len(topo_order) == numCourses else []