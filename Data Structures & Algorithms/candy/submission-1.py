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
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                res[i] += 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] += 1

        return sum(res)

        