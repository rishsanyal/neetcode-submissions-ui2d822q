"""
We go through each string and iterate through it until it matches

"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ''

        prefix = strs[0]

        for word in strs:
            itr_len = min(len(word), len(prefix))
            res = ''

            for i in range(itr_len):
                if word[i] != prefix[i]:
                    break
                
                res += word[i]

            prefix = res

        return prefix