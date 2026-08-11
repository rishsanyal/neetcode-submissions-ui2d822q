"""
at each level, we could either have a word be in wordDict or be a part of a bigger word from wordDict

if we see a match, we add that to the list of seen words and recurse with that
then we continue as normal

we track idx, current word, previous words

if no match for current word, we add it to idx

----

if match:
    we can start a new word

then we add it to idx


"""



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []

        wordSet = set(wordDict)


        def r(idx, curr_word, prev_words):
            if idx == len(s):
                if not curr_word:
                    res.append(' '.join(prev_words[:]))
                    
                return

            if curr_word + s[idx] in wordSet:
                r(idx+1, '', prev_words+[curr_word + s[idx]])

            r(idx+1, curr_word + s[idx], prev_words)

            return

        r(0, '', [])

        return res