"""
Array is weird, there's a point where everything's either increasing or decreasing

no point in finding the pivot - WRONG
We could find the pivot and then search the left of that
AND search the right of it

we maintain a tracker for the min index of the number

maybe caching later
"""

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        l, r = 0, n-1

        tracker = n
        mid = n

        # Find Pivot

        while l <= r:
            mid = (l+r)//2
            num_mid = mountainArr.get(mid)

            num_l, num_r = mountainArr.get(mid-1), mountainArr.get(mid+1)

            if num_l < num_mid < num_r:
                l = mid + 1
            elif num_l > num_mid > num_r:
                r = mid - 1
            else:
                break

        # mid is pivot
        pivot = mid

        # search left for target
        l, r = 0, pivot

        while l <= r:
            mid = (l+r)//2
            num_mid = mountainArr.get(mid)

            num_l, num_r = mountainArr.get(l), mountainArr.get(r)

            if num_mid == target:
                r = mid - 1
                tracker = min(tracker, mid)
            elif num_l <= target <= num_mid:
                r = mid - 1
            else:
                l = mid + 1

        
        # search right
        l, r = pivot, n-1

        while l <= r:
            mid = (l+r)//2
            num_mid = mountainArr.get(mid)

            num_l, num_r = mountainArr.get(l), mountainArr.get(r)

            if num_mid == target:
                r = mid - 1
                tracker = min(tracker, mid)
            elif num_l >= target >= num_mid:
                r = mid - 1
            else:
                l = mid + 1        

                    
        return tracker if tracker != n else -1