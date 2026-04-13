class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        - We have to compare the longest word - N Times
        - It has to be O(MN)

        - ['abc', 'abc', 'abd'] -> ab
        """

        if not strs:
            return ''

        result = strs[0]

        for word in strs[1:]:
            comparison_length = min(len(word), len(result))
            previous_result = result[:comparison_length]
            result = ''

            for idx in range(comparison_length):
                if previous_result[idx] != word[idx]:
                    break
                result += previous_result[idx]

        return result