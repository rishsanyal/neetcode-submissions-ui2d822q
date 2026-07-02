class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        tracker = defaultdict(int)
        res = -1

        for idx, c in enumerate(s):
            if c not in tracker:
                tracker[c] = idx
                continue
            
            res = max(
                res,
                idx - tracker[c] - 1
            )

        return res
            