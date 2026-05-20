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
        l, r = 0, len(arr)-1

        while (r-l) >= k:
            if abs(arr[r] - x) < abs(arr[l] - x):
                l += 1
            else:
                r -= 1

        return arr[l:r+1]