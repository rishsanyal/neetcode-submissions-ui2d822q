"""

- Median is the number in the middle in a sorted array
- we could add all arrays into 1 and go from there but that won't help

Whichever list is longer, is more likely to have the median in it
median -> ((r1+r_2) - (l_1+l_2)) // 2

- we have 4 trackers, l_1, m_1, r_1, l_2, m_2, r_2
- we move the trackers towards the middle number
- it's about the length of the array, right?
- if nums[m2] > nums[m1]

We take the middle of the sum of both 
"""



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        a,b = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        l, r = 0, len(a)-1


        while True:
            mid = (l+r)//2
            big_mid = half - mid - 2 # This lands us in the left half of the bigger list

            l1 = a[mid] if 0 <= mid else float('-inf')
            r1 = a[mid+1] if mid+1 < len(a) else float('inf')

            l2 = b[big_mid]if 0 <= big_mid else float('-inf')
            r2 = b[big_mid+1] if big_mid+1 < len(b) else float('inf')

            if l1 <= r2 and l2 <= r1:
                if total % 2:
                    return min(r1, r2)
                else:
                    return float(max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                r -= 1
            else:
                l += 1

        return 0



