"""
We pop it all in a max heap
pop k elements


[2,3,1,5,4]
[5,4,3,2,1] k = 2

sort and len(nums)-kth index
"""



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []

        nums.sort()

        if len(nums)-k > 0:
            return nums[len(nums)-k]
        
        return -1
