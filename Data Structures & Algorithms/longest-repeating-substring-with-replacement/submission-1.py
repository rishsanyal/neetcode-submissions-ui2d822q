class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        res = 0
        start = end = 0

        ctr = defaultdict(int)

        while end < len(s):
            ctr[s[end]] += 1

            max_freq = max(max_freq, ctr[s[end]])

            while (start - end + 1 - k) > max_freq:
                ctr[s[start]] -= 1
                start += 1

            res = max(res, end-start+1)
            end += 1

        return res