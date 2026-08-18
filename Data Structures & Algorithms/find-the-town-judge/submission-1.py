class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        return label of town judge, else return -1
        - judge:
        - no outgoing edges
        - n-1 incoming edges
        will only have one judge

        idea:
        if there is a judge, everyone else will have an outgoing edge. 
        so bias checking outgoing edge first. the one with no outgoing is the judge
            - there should only be one. else it is 

        Solution
        instead of keeping an incoming list and outgoing list, combine together as a score
        score = trust_received - trust_given
        the judge should have a score of n - 1 trust received with no trust given
        - a person can trust multiple people but it can't receive more than n - 1 trusts
            - if it gives out even just one, it will be less than n-1 and not optimal
        note: 1-indexed
        """  

        score = [0] * (n + 1) # trust received - trust given out
        # 1) populate score
        for giver, receiver in trust:
            score[giver] -= 1
            score[receiver] += 1

        for i in range(1, n + 1):
            if score[i] == n - 1:
                return i
        
        return -1


