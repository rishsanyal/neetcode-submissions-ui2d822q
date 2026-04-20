class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search in a rotated array

        the number is either between mid and end or on left
        
        if target > nums[mid] and target < nums[r]:
            go right
        elif target > nums[mid] and target > nums[r]:
            go left
        elif target < nums[mid] and target > nums[l]:
            go left
        if target < nums[mid] and target < nums[l]:
            go right
        elif target == nums[mid]:
            return mid
        elif target == nums[l]:
            return l
        elif target == nums[r]:
            return r
        else:
            print("SAVE ME")

        we know how to find the min but not a specific number
        atleast it's sorted

        1 solution:
            - Double the array
            - find the smallest number on the left
            - find the largest number of the right
            - binary search between that and calculate the index from there
        
        But O(N) space, which we probably don't want
        O(N) time to find min and max too
        """

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if target > nums[mid] and target < nums[r]:
                # go right
                l = mid + 1
            elif target > nums[mid] and target > nums[r]:
                # go left
                r = mid - 1
            elif target < nums[mid] and target > nums[l]:
                # go left
                r = mid - 1
            if target < nums[mid] and target < nums[l]:
                # go right
                l = mid + 1
            elif target == nums[mid]:
                return mid
            elif target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            else:
                print("SAVE ME")

        return -1