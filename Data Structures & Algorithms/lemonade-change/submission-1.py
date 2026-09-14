class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        15 Sep 2026
        - return true if you can provide correct change to every customer

        idea
        - keep track of current money and see if can give change
        - greedily use the largest value first as it is the hardest to return
        - easy:
            bills is either 5, 10 or 20
        - if change >= 20 and there is 20, use it. Else use 10, else use 5. Else invalid
        - if change >= 10 and got 10, uset it. Else use 5. Else invalid
        - else use 5 if have

        - also there is no way to give 20 as a change so ignore it
            - possible bills 5,10,20 -> possible changes 0, 5, 15
        the bill received, keep it as is

        mistake: $10 bill is one piece, can't be spit to 2 $5
        """
        n = len(bills)
        bill_counts = {5:0, 10:0} # skip 20 as it can't be used as change

        for i in range(n):
            bill = bills[i]
            if bill == 5: # no change needed
                bill_counts[5] += 1
            elif bill == 10: # need change of $5
                if bill_counts[5]:
                    bill_counts[5] -= 1
                    bill_counts[10] += 1
                else:
                    return False
            else: # bill = 20(unable to use as change) -> need $15 
                if bill_counts[10] and bill_counts[5]: # use 10 and 5
                    bill_counts[10] -= 1
                    bill_counts[5] -= 1
                elif bill_counts[5] >= 3: # 3 fives
                    bill_counts[5] -= 3
                else:
                    return False
            
        return True # reach here means no false