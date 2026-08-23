class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        - return min no of operations (convert white -> black) to get at least one
        occurrence of k consecutive black blocks

        Idea - consecutive (sliding window)
        - maintain window of size k
        - find the subarray with the max count of black. 
        - k - max_count_black_in_subarray = no of operations
        """
        n = len(blocks)

        # 1) init window
        black_count = 0 # sliding window
        for i in range(k):
            if blocks[i] == "B":
                black_count += 1
 
        max_black_count = black_count
        # 2) main sliding window
        for i in range(k, n): # k - 1 + 1
            if blocks[i] == "B": # Add new
                black_count += 1
            if blocks[i - k] == "B": # Remove back
                black_count -= 1
            max_black_count = max(max_black_count, black_count)

        return k - max_black_count


