"""
Sort both and track the pointer
(nlg(n)) time
O(1) space

counters for both and compare keys and values
constant space
O(n) time

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_ctr = Counter(s)
        t_ctr = Counter(t)

        for key, val in s_ctr.items():
            if key not in t_ctr or t_ctr[key] != val:
                return False

        return True