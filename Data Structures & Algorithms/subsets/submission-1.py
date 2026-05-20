"""
At every level, we have 2 options
- We pick one
- We don't

base case: when there's no more list left, return the list

We have a universal list
function(idx, curr_list):
    if idx >= len(inp_list):
        return

    global_list.append(curr_list)

    function(idx+1, curr_list+list[idx])
    function(idx+1, list[idx])

    


    
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.res = []
        
        def track(idx, curr_list):
            if idx >= len(nums):
                self.res.append(curr_list)
                return

            track(idx+1, curr_list+[nums[idx]])
            track(idx+1, curr_list)

        track(0, [])

        return self.res