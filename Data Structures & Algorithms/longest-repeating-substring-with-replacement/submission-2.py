"""
We keep a rolling dict
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        res = 0
        start = end = 0

        ctr = defaultdict(int)

        while end < len(s):
            ctr[s[end]] += 1

            max_freq = max(ctr.values())

            # We check every window with K transformations
            while (end - start + 1 - max_freq) > k:
                ctr[s[start]] -= 1
                start += 1

            # We update the result
            res = max(res, end-start+1)
            end += 1

        return res