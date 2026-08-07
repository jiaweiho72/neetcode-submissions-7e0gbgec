class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        19 july 2026
        - return min time for all n node to receive the signal from k
        - if impossible for all to receive -> return 1

        weighted with time -> dijsktra shortest path
        - build adj_list
        - init distances list with infinity
        - priority queue (minheap) popping the shortest path (distance, node)
            - process the current shortest distance
                - visit neighbours
                    - new_distance = add current node distance and the neighbour distance
                    - if new_distance < distance[neighbour] then update the smaller value
            - visited set to prevent reprocessing alr processed nodes
        - outputs a list of min distance from k

        - from the distances, return the min. If still has infinity -> impossible

        concept: PQ we process the global shortest everytime as we have greater certainty that it is the local shortest path for next node calculation (there may be shorter down the line). If it chose the longer node, the next node calculation will be wrong. Basically greedy minimum, guranteed minimum from this edge source to the next node
        """


        # 1) Build adj_list
        adj_list = [[] for _ in range(n + 1)] # 1 indexed
        for u, v, w in times:
            adj_list[u].append((v, w))
        
        # 2) Djisktra
        def dijkstra(node):
            import heapq
            distances = [float('inf')] * (n + 1)
            min_heap = [(0, k)] # initial distance to itself is 0
            distances[k] = 0
            visited = set()

            while min_heap:
                cur_dist, cur_node = heapq.heappop(min_heap)
                if cur_node in visited: # already processed
                    continue
                visited.add(cur_node)
                # visit neighbours
                neighbours = adj_list[cur_node]
                for v, w in neighbours:
                    new_dist = cur_dist + w
                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        heapq.heappush(min_heap, (new_dist, v))
            return distances[1:]
        timings = dijkstra(k)
        max_time = float('-inf')
        for i in range(len(timings)):
            if i == (k - 1):
                continue
            timing = timings[i]
            if timing == float('inf'):
                return -1
            max_time = max(max_time, timing)

        return max_time
