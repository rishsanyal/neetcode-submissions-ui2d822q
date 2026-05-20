"""
Iterate with a set of characters and len(s1) through s2
if the set matches, we compare and find if true

if the set is equal, we compare dicts. Can we compare dicts directly in python? - YES

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_dict = Counter(s1)

        s2_dict = Counter(s2[:len(s1)])
        num_pop = 0

        for i in range(len(s1), len(s2)):
            if s1_dict == s2_dict:
                return True
            
            if i >= len(s1):
                s2_dict[s2[num_pop]] -= 1

                if s2_dict[s2[num_pop]] <= 0:
                    s2_dict.pop(s2[num_pop])

                num_pop += 1
                
            s2_dict[s2[i]] += 1

        return s2_dict == s1_dict