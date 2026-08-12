"""

3 sum with 2 loops?

[-3,0,1,2,3,3]
 l      m    r

We need unique quadruplets
How do we get those? we check m and r
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

                l, r = left+1, right-1

                while l < r:
                    curr_num = nums[left] + nums[l] + nums[r] + nums[right]

                    if curr_num == target:
                        res.append(
                            [nums[left], nums[l], nums[r], nums[right]]
                        )

                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l+1]:
                            l += 1

                        while r > l and nums[r] == nums[r-1]:
                            r -= 1
                    elif curr_num > target:
                        r -= 1
                    else:
                        l += 1

        return res

                