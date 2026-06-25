"""
We could make a Trie of the words in dict
- O(N) N is the sum of characters

"""


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        trie = {}
        curr_tracker = trie

        for word in dictionary:
            curr_tracker = trie

            for char in word:
                if char not in curr_tracker:
                    curr_tracker[char] = {}

                curr_tracker = curr_tracker[char]

            curr_tracker['#'] = {}

        res = len(s)
        curr_tracker = trie

        last_word_idx = 0

        for idx, char in enumerate(s):
            if char not in curr_tracker:
                print(char, last_word_idx)
                res = len(s) - last_word_idx - 1
                return res

            curr_tracker = curr_tracker[char]

            if '#' in curr_tracker:
                print(char)
                last_word_idx = idx

        return 0
            

