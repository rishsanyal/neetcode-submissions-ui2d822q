"""
nums1 = [10,20,20,40,50,50]
nums2 = [50, 50]



Greater number goes in the end index
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """


        last_index = m+n-1

        l, r = m-1, n-1

        while l >= 0:
            if nums1[l] > nums2[r]:
                nums1[last_index], nums1[l] = nums1[l], 0
                l -= 1
            else:
                nums1[last_index], nums2[r] = nums2[r], 0
                r -= 1
            
            last_index -= 1

        while r >= 0:
            nums1[last_index] = nums2[r]
            r -= 1

        print(nums1)


        
        


