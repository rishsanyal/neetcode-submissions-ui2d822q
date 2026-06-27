"""
We could have a heap and keep circling through int


There has to be something mathematical here
We just have to make sure that the guy with the lowest rating gets -1 amount of candy than others

not exactly, people of the same rating can get different candies

We give everyone 1 candy
we iterate through the list and check each number's neighbors and award candies with the highest number among 3 elements

"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        arr = [1] * n

        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                arr[i] = arr[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                arr[i] = max(arr[i], arr[i + 1] + 1)

        return sum(arr)