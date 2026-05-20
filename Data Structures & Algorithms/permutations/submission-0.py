class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def r(remaining_list, curr_list):
            if len(curr_list) == len(nums):
                res.append(curr_list)
                return

            for i in range(len(remaining_list)):
                r(remaining_list[:i]+remaining_list[i+1:], curr_list+[remaining_list[i]])

        r(nums, [])

        return res

            

