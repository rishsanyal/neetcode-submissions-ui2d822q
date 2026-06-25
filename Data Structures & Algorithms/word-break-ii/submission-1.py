"""

we need to check if [current index: current index + len(word)] is in the word dict
if so, we add to a list

if not, we continue to the next word


base case: When the index == len(s) we add to a global result list

def dfs(curr_idx, inp_list=[]):
    if curr_idx == len(s):
        result.append(inp_list[:]) # because we need to make a copy

    if curr_idx > len(s):
        return

    for word in wordDict:
        if s[curr_idx: curr_idx + len(word)] in wordDict:
            dfs(curr_idx + len(word) - 1, inp_list + [word])
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        wordSet = set(wordDict)

        def dfs(curr_idx, inp_list=[]):
            if curr_idx == len(s):
                print(inp_list)
                result.append(' '.join(inp_list[:]))

            if curr_idx > len(s):
                return

            # # len(wordSet) - O(M)
            # for word in wordSet:
            #     # len(word) - sum of all words
            #     if s[curr_idx: curr_idx + len(word)] == word:
            #         dfs(curr_idx + len(word), inp_list + [word])

            for j in range(curr_idx, len(s)):
                word = s[curr_idx: j]

                if word in wordSet:
                    dfs(j+1, inp_list + [word])

        dfs(0, [])
        
        return result