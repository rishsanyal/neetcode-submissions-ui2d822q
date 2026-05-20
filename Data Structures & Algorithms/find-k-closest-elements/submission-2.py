"""
We could totally use a MIN heap for this

Iterate through the list, check abs value and push on heap - nlg(n) time because of heapifying

We could sort and go back and forth from the middle?
If we have a sorted list, we could drill down on the closest window
We could also sort it using a custom function and pick the first few elements, right?

We have l and r from a sorted list
We could iterate through the list and check the sum of difference between the first and last element of the window


"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k
        start = 0
        min_diff = float('inf')

        for i in range(0, len(arr)):
            if (i + k) <= len(arr):
                new_diff = abs(arr[i] - x) + abs(arr[i+k-1] - x)

                if new_diff <= min_diff:
                    min_diff = new_diff
                    l, r = i, i+k
        
        return arr[l:r]
