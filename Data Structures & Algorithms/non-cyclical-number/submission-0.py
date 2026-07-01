"""

We need a visited set to track where we've been
we need to keep going until we either see something in the set or we hit 1
"""

class Solution:
    def isHappy(self, n: int, visited_set=set()) -> bool:
        if n == 1:
            return True

        if n in visited_set:
            return False

        new_num = 0
        curr_num = n

        while curr_num // 10:

            temp_num = curr_num % 10
            new_num += temp_num*temp_num

            curr_num = curr_num // 10

            if not curr_num // 10:
                temp_num = curr_num % 10
                new_num += temp_num*temp_num

        return self.isHappy(new_num, visited_set | set([curr_num]))
                
            
