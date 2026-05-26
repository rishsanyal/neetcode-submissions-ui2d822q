"""
Make a set of wordDict

for each index we have 2 options:
    if curr_idx == len(s):
        return True

1. if curr_idx + len(word) <= s and s[curr_idx: curr_idx + len(word)] in wordDict
    we keep going

"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)

        def r(curr_idx):
            if curr_idx > len(s):
                return False

            if curr_idx == len(s):
                return True

            for curr_word in wordDict:
                curr_word_check = s[curr_idx: curr_idx+len(curr_word)]

                if curr_word_check in wordDict:
                    res = r(curr_idx+len(curr_word))
                    if res:
                        return True

            return False
        
        return r(0)

        