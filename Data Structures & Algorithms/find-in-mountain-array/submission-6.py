"""

It's like a rotated sorted array, maybe

3 cases
we're on the left: arr[mid-1] < arr[mid] < arr[mid+1]
    if num == mid:
        return mid
    if num < mid:
        go left
    if num > mid:
        go right

we're in the middle: arr[mid-1] < arr[mid] > arr[mid+1]
    if num < mid:
        go left or right?
    elif num > mid:
        not possible
    elif num == mid:
        return mid

we're on the right: arr[mid-1] > arr[mid] > arr[mid+1]
    if num == mid:
        return mid
    if num < mid:
        go right
    if num > mid:
        go left


We could find pivot and then split the problem from there

1. Find pivot: (lg(n))
    we're on the left: go right
    we're on the right: go left
    return mid

2. Find in 2 subarrays (lg(n))


"""



class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        arr_len = mountainArr.length()

        def find_pivot():
            l, r = 0, arr_len-1

            while l <= r:
                mid = (l+r)//2

                left_num, right_num = mountainArr.get(mid-1) if mid > 0 else 0, mountainArr.get(mid+1) if mid < arr_len else arr_len-1
                curr_num = mountainArr.get(mid)

                if left_num < curr_num < right_num:
                    l = mid + 1
                elif left_num > curr_num > right_num:
                    r = mid - 1
                else:
                    return mid

            return -1

        def __bs(l, r):
            while l <= r:
                mid = (l+r)//2
                num_mid = mountainArr.get(mid)

                if num_mid == target:
                    return mid
                elif num_mid < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return float('inf')

        def __bs_reverse(l, r):
            while l <= r:
                mid = (l+r)//2
                num_mid = mountainArr.get(mid)

                if num_mid == target:
                    return mid
                elif num_mid < target:
                    r = mid - 1
                else:
                    l = mid + 1

            return float('inf')

        pivot = find_pivot()

        ans = min(
            __bs(0, pivot),
            __bs_reverse(pivot, arr_len-1)
        )

        return ans if ans != float('inf') else -1
        