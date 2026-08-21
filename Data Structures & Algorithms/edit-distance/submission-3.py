"""

- We'll need n+1 rows and m+1 columns
- because since we can insert characters, if w1 is empty, we'll need to insert characters

  X m o n k e y s
X 0 1 2 3 4 5 6 7
m 1 0 1 2 3 4 5 6
o 2 1 0 1 2 3 4 5
n 3 2 1 0 1 2 3 4
e 4 3 2 1 2 1 2 3
y 5 4 3 2 3 2 1 2

Thanks for a smaller solution

  X n e 
X 0 1 2 
n 0 0 1 
e 1 1 0 
e 2 2 1 
t 3 3 2


"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        cache = [([0 for _ in range(len(word1)+1)]) for _ in range(len(word2)+1)]

        for i in range(len(word2)+1):
            cache[i][0] = i

        for i in range(len(word1)+1):
            cache[0][i] = i

        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                curr_w2_char = word2[i-1]
                curr_w1_char = word1[j-1]

                if curr_w1_char == curr_w2_char:
                    cache[i][j] = cache[i-1][j-1]
                else:
                    cache[i][j] = 1 + min(cache[i-1][j], cache[i][j-1], cache[i-1][j-1])

        return cache[-1][-1]