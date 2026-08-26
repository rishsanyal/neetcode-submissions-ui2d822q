"""
we can do this in 2 passes
left-right -> 1, len(ratings)
right-left -> (len(ratings)-2, 0)


[1,1,1]

[4,3,5]
[1,1,2]
[2,1,2] -> 5

[1,1,1]
[2,3,3]
[1,2,1]
[1,2,1] - 4

float('inf') + [1,3,2,2,1] + float('inf')

[inf,1,2,3,4,5,inf]
[1,1,2,3,4,5,1]
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                res[i] = res[i - 1] + 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                # THIS IS THE ERROR CASE
                res[i] = max(res[i], 1 + res[i+1])

        return sum(res)

        