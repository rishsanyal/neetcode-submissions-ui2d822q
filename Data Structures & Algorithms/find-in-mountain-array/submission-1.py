"""
Array is weird, there's a point where everything's either increasing or decreasing

no point in finding the pivot

we maintain a tracker for the min index of the number

find, num_l, num_mid, num_r
3 calls per turn

if num_l == num_mid == num_r:
    # go left
elif num_l <= num_mid:
    if num_l <= target <= num_mid:
        go left
    else:
        go right
else:
    if num_mid <= target <= num_r:
        go right
    else:
        go left

everytime we go left, we check if num_mid == target and compare

how do we ensure under 100 calls? - not sure
"""

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        l, r = 0, n-1

        tracker = n

        while l < r:
            num_l, num_r = mountainArr.get(l), mountainArr.get(r)
            mid = (l+r)//2
            num_mid = mountainArr.get(mid)


            if num_l <= num_mid:
                if num_l <= target <= num_mid:
                    r = mid - 1

                    if num_l == target:
                        tracker = min(tracker, l)
                    if num_mid == target:
                        tracker = min(tracker, mid)
                else:
                    l = mid
            else:
                if num_mid <= target <= num_r:
                    l = mid

                    if num_mid == target:
                        tracker = min(tracker, mid)
                    if num_r == target:
                        tracker = min(tracker, r)
                else:
                    r = mid - 1
        return tracker if tracker != n else -1