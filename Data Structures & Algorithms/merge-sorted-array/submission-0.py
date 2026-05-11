class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Have have to do it constant space
        we could swap out numbers constantly
        when we reach m in nums1, we know to add nums2

        nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2

        l, r = 0, 0

        [10,20,20,40,0,0], [1,2]



        we need to track the smaller list and compare against that? - maybe

        we could just append and sort (nlg(n))

        we use 3 pointers:
        - tracking the last index of nums1
        - tracking m
        - tracking n

        if nums1[m] <= nums2[n]:
            we add the number to last
            last -= 1
            n -= 1
        else:
            switch

        """


        last_idx = (m+n-1)
        big_idx, small_idx = m-1, n-1
        
        while small_idx >= 0:
            if big_idx >= 0 and nums1[big_idx] > nums2[small_idx]:
                nums1[last_idx] = nums1[big_idx]
                big_idx -= 1
            else:
                nums1[last_idx] = nums2[small_idx]
                small_idx -= 1

            last_idx -= 1

        