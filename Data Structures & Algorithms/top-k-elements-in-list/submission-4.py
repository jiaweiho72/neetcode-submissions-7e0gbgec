class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        2 oct 2026
        - brute force. heap nlogn

        - optimal 
            - array and index is the count
            - bucket sort: makes sense as you are sorting by count
                - if you are just sorting numbers, every index is a number?

        time: O(n)
        space: O(n)
        11 mins
        """
        from collections import Counter
        n = len(nums)

        # 1) count
        count_dict = dict(Counter(nums))
        counts = [[] for i in range(n + 1)]
        for num, count in count_dict.items():
            counts[count].append(num)
        
        # 2) extract the top k
        rank = 0
        result = []
        for i in range(n -1+1, -1, -1):
            cur_counts = counts[i]
            for j in range(len(cur_counts)):
                rank += 1
                result.append(cur_counts[j])
                if rank == k:
                    return result
        return result
            








        """
        3 apr 2026
        - get count
        - getting top k
            - max heap is either klogn or nlogk which is higher than n
        return list of top k
        """

        from collections import Counter

        n = len(nums)
        count_dict = dict(Counter(nums))
        
        # array where index is count and element is list of numbers with that count
        frequency_arr = [[] for _ in range(n + 1)] # + 1 as count is up to n

        for num, count in count_dict.items():
            frequency_arr[count].append(num)

        topk_list = []

        # iterate in reverse -> top k
        for i in range(len(frequency_arr) - 1, -1, -1):
            cur_list = frequency_arr[i]
            for cur in cur_list:
                topk_list.append(cur)
                k -= 1
                if k == 0:
                    return topk_list            
            
        
        



