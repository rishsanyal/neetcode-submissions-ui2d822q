"""

- We use a two pointer approach
- We sort the list
- We set the l=0, r=len(nums)-1 and have another pointer between l+1 and r-1
- We keep going until nums[l] + nums[mid] + nums[r] <= 0
- we either increase l or reduce r depending on which one's closer to 0

WRONG

[-1,0,1,2,-1,-4]

[-4,-1,-1,0,1,2]


"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums) - 1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                if curr_sum < 0:
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1


                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res
        