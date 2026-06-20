"""
Everything increases and then everything decreases

we need to make 3 calls per num 
33 times

4.lg(10) = 4

we could maybe cache the number too
"""


class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        r = mountainArr.length() - 1

        n = 0

        if r < 3:
            return -1

        l = 0
        mid = 0

        while l <= r:
            mid = l + (r-l)//2
            n += 1

            left_num, mid_num, right_num = mountainArr.get(l), mountainArr.get(mid), mountainArr.get(r)

            if left_num < mid_num < right_num:
                l = mid + 1
            elif left_num > mid_num > right_num:
                r = mid - 1
            else:
                # print(l, r)
                # print( left_num, mid_num, right_num)
                # print(n)
                break

        l, r = 0, mid

        while l <= r:
            mid = l + (r-l)//2
            num = mountainArr.get(mid)

            if num == target:
                return mid
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1

        l, r = mountainArr.length() - 1, mid

        while l >= r:
            mid = r + (l-r)//2
            num = mountainArr.get(mid)

            if num == target:
                return mid
            elif num < target:
                r = mid + 1
            else:
                l = mid - 1

        return -1


