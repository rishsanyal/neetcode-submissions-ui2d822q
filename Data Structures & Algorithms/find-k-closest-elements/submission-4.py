"""

- We take the difference of each element
- throw it in a heap

- but it's already sorted, so we can use that somehow
- whichever index has the lowest difference is our center
- we either pick k elements with i as the center
    - make up the difference on the side with more elements
- we'll need to compare the array with all the elements


[2,4,5,8], 2 6
[
    [2,4] - [4, 2] - 6
    [4,5] - [2, 1] - 3
    [5,8] - [1, 2] - 3
]

[2,3,4,5,6] x = 1
[
    4, 0
    
    [3, 5] - 8
]

difference, l

"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import heapq

        # heap -> difference, l
        difference = []

        for i in range(len(arr)-k+1):
            l = i
            r = i + k - 1

            heapq.heappush(
                difference,
                (
                    abs(x - arr[l]) + abs(x - arr[r]),
                    l
                )
            )

        _, min_diff_l = heapq.heappop(difference)

        # print(min_diff_l)
        # print(arr, l, k)

        return arr[min_diff_l:min_diff_l+k]







        