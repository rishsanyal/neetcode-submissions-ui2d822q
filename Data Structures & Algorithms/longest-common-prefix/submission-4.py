class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        - We have to compare the longest word - N Times
        - It has to be O(MN)

        - ['abc', 'abc', 'abd'] -> ab
        """

        prefix = ''
        for i in range(len(strs[0])):
            for curr_word in strs:
                if i == len(curr_word) or curr_word[i] != strs[0][i]:
                    return prefix

            prefix += strs[0][i]

        return prefix