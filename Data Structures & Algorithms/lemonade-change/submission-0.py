"""
We can either have 2 5's or 1 10
how do we 
"""

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        change_tracker = {20:0, 10:0, 5:0}

        for idx, bill in enumerate(bills):
            if bill == 5:
                change_tracker[5] += 1
            else:
                change = bill - 5

                while change_tracker[20] and (change >= 20):
                    change_tracker[20] -= 1
                    change -= 20
                while change_tracker[10] and (change >= 10):
                    change_tracker[10] -= 1
                    change -= 10
                while change_tracker[5] and (change >= 5):
                    change_tracker[5] -= 1
                    change -= 5

                if change > 0:
                    return False

                change_tracker[bill] += 1

        return True

        
