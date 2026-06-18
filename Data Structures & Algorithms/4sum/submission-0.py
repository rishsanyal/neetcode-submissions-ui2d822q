"""

4Sum approach

- Sort the list
- res = []

- for right in range(len(nums)-1, -1, -1):
    - for left in range(0, right):
        - l,r = left+1, right-1
        - while l < r:
            - curr_sum = nums[left] + nums[l] + nums[r] + nums[right]
            - if curr_sum == target:
                res.add((nums[left], nums[l], nums[r], nums[right]))
                l += 1
                r -= 1
            - elif curr_sum < target:
                l += 1
            - elif curr_sum > target:
                r -= 1

            while r > l and nums[r] == nums[r+1]:
                r -= 1
            
            while l < r and nums[l] == nums[l-1]:
                l += 1




[-3, 0, 1, 2, 3, 3]

right, left, l, r
-3, 3, 0, 3 - res
-3, 3, 1, 2 - res


"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []

        for right in range(len(nums)-1, -1, -1):
            
            if right < len(nums)-1 and nums[right] == nums[right+1]:
                continue

            for left in range(right):
            
                if left > 0 and nums[left] == nums[left-1]:
                    continue

                l,r = left+1, right-1

                while l < r:
                    curr_sum = nums[left]+nums[l]+nums[r]+nums[right]

                    if curr_sum == target:
                        res.append((nums[left],nums[l],nums[r],nums[right]))

                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l-1]:
                            l += 1

                        while r > l and nums[r] == nums[r+1]:
                            r -= 1

                    elif curr_sum > target:
                        r -= 1
                    else:
                        l += 1
        return res



















        