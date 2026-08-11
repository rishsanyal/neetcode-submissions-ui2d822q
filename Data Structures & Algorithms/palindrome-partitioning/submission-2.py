"""

We track idx, curr word, curr palindromes

if curr_word+s[idx] is a palindrome
    r(idx+1, '', curr_palindromes+[curr_word+s[idx]])

r(idx+1, curr_word+s[idx], curr_palindromes)

"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def r(idx, curr_word, curr_palindromes):
            if idx == len(s):
                # if curr_word and curr_word == curr_word[::-1]:
                #     res.append(curr_palindromes + [curr_word])
                
                if not curr_word:
                    res.append(curr_palindromes)

                return


            new_word = curr_word + s[idx]

            if new_word == new_word[::-1]:
                r(idx+1, '', curr_palindromes+[new_word])

            r(idx+1, new_word, curr_palindromes)

            return

        r(0, '', [])

        print(res)

        return res
        