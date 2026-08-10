class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Dynamic Programming
        - dp(i1, i2)
            - fact: i3 = i1 + i2
            - don't have to worry about '|n - m| <= 1' as it naturally works out
                - any choice and it will still be satisfying this condition
        - dp returns boolean if the remaining is valid
        """
        
        from functools import cache

        # 1) Check that lengths are valid
        if len(s1) + len(s2) != len(s3):
            return False
        
        # 2) Main DP
        @cache
        def dfs(i1, i2):
            if i1 == len(s1) and i2 == len(s2): # reached the end successfully
                return True
            
            i3 = i1 + i2
            
            # try to take from s1
            if i1 < len(s1) and s1[i1] == s3[i3]:
                if dfs(i1 + 1, i2):
                    return True

            # try to take from s2
            if i2 < len(s2) and s2[i2] == s3[i3]:
                if dfs(i1, i2 + 1):
                    return True

            return False
        return dfs(0, 0)


        
        """
        Bottom UP
        """
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
        
        