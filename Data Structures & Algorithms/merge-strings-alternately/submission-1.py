class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)

        res = ""

        i, j = 0, 0
        status = True

        while (i < m) and (j < n):
            if status:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1

            status = not status

        if (i < m):
            res += word1[i:]

        if (j < n):
            res += word2[j:]

        return res
            