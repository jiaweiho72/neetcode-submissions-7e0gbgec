class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
            
        
        



