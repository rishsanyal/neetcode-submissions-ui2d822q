"""
- No duplicate triplets

- Sort the list
- We have l = 0, r = len(nums)-1 and m from l+1 to r-1
- if l > 0 and nums[l] == nums[l+1]: we skip using that as l

"""



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []

        for l in range(0, len(nums)-2):
            if 0 < l and nums[l] == nums[l-1]:
                continue

            if l >= len(nums)-1:
                break

            r = len(nums)-1
            m = l+1

            while m < r:
                curr_num = nums[l] + nums[m] + nums[r]

                if curr_num == 0:
                    res.append([nums[l], nums[m], nums[r]])

                    m += 1
                    
                    while (m < r) and nums[m] == nums[m-1]:
                        m += 1

                elif curr_num > 0:
                    r -= 1
                else:
                    m += 1


        return res

            



