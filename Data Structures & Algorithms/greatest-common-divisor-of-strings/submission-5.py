"""
We start with an empty str

we check if the entire string can be divided, if so, we're good

Should we check the smaller string first?

__helper(comparison_str, divisor):

    return bool

for i in range(len(str2)):
    res += str2[i]

    if __helper(str2, res) and __helper(str1, res):
        gcs = res

return gcs
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        gcs = ''
        res = ''

        def __helper(comparison_str, divisor):
            comparison_str_idx = 0

            while comparison_str_idx < len(comparison_str):
                if comparison_str[comparison_str_idx: comparison_str_idx + len(divisor)] != divisor:
                    return False

                comparison_str_idx += len(divisor)

            return bool(comparison_str_idx == len(comparison_str))

        for i in range(len(str2)):
            res += str2[i]
            if __helper(str2, res) and __helper(str1, res):
                gcs = res

        return gcs
        