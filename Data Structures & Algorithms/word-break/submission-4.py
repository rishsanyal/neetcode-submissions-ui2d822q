"""
convert wordDict into wordSet for easier lookup
at each index, we start a new word or add the character to the previous word

start_idx = 0

if start_idx == len(s):
    return True

for each word in wordSet:
    if start_idx + len(word) >= len(s):
        return False

    if the first n characters match word:
        status = r(start_idx + len(word))

        if status:
            return True

return False


"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        cache = {}
        word_set = set(wordDict)
        
        def r(start_idx=0):
            if start_idx == len(s):
                return True

            if start_idx in cache:
                return cache[start_idx]

            cache[start_idx] = False

            for word in word_set:
                if start_idx + len(word) > len(s):
                    continue

                if s[start_idx: start_idx + len(word)] == word:
                    status = r(start_idx + len(word))
                    cache[start_idx] = status

            return cache[start_idx]

        return r(0)
