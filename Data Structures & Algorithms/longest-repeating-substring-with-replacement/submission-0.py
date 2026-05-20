"""
We have a left counter and right counter
we could keep replacing the top of the min heap with K operations?

We could maintain a rolling heap but might be an issue


We use start and end pointers
The math is the magic here

end - start + 1 - 2 <= k
4 - 0 + 1 - 2 <= 4 -> False

- Add count to tracker
- check current max frequency 
- end - start + 1 - max_frequency > k 
    -> Means it takes more than removing the 
        rest of the characters other than the 
        max frequency to make the string homogenous
    -> It's weird because the max_freq can change if the start changes
    -> But then it'll go into negative also we still have max_freq-1 which works for us

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ctr = defaultdict(int)
        start = end = 0
        res = 0

        max_freq = 0

        while end < len(s):
            ctr[s[end]] += 1

            max_freq = max(max_freq, ctr[s[end]])

            while (end - start + 1 - max_freq) > 0:
                ctr[s[start]] -= 1
                start += 1

            res = max(res, end-start+1)
            end += 1

        return res