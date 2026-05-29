class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]

        for i in range(len(word1)+1):
            cache[0][i] = i

        for i in range(len(word2)+1):
            cache[i][0] = i
        

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                print(i, j)
                if word1[i-1] == word2[j-1]:
                    cache[i][j] = cache[i-1][j-1]
                else:
                    cache[i][j] = 1 + min(cache[i-1][j], cache[i][j-1], cache[i-1][j-1])

        print(cache)
