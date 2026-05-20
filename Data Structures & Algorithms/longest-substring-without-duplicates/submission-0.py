"""
We have a l pointer and r pointer
we maintain a set while iterating
if we run into a character that is in the set, we keep popping elements off the set 
    until we see the change

    ISSUE: SETs don't maintain order -> use a dict

zxyzxyz
xyz
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        tracker = set()

        res = 0

        while l <= r and r < len(s):
            curr_char = s[r]

            while curr_char in tracker:
                char_to_pop = s[l]
                tracker.remove(char_to_pop)
                l += 1
            
            tracker.add(curr_char)
            res = max(res, r-l+1)


            r += 1

        return res