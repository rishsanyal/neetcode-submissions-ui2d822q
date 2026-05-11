class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        We have the min and the max

        let's assume valid cases
        Should be in the realm of set-iteration

        iterate through, find the min and the max
        keep iterating from the min to go and find the max

        O(N) time
        O(N) Space

        How do we do this in O(1) space?
        - we use the list as a way to mark the seen indices

        - We disregard everything below 0
        - we iterate through the list
            - We if we don't see the first index populated, then we know the number missing is 1
            - If the number is OOB, we won't mark it


        [1,2,3,7]
        [-1, -2, -3, 7] -> 4
        """

        min_num, max_num = 0, 0

        for idx, val in enumerate(nums):
            if val < 0:
                nums[idx] = 0
            
            min_num = min(min_num, val)
            max_num = max(max_num, val)

        min_num = max(min_num, 1)

        for _, val in enumerate(nums):
            # print(nums)
            if 0 <= abs(val)-1 < len(nums):
                curr_num = abs(val)-1
                if nums[curr_num] == 0:
                    nums[curr_num]= -1
                else:
                    nums[curr_num] = -1*nums[curr_num] if nums[curr_num] > 0 else nums[curr_num]

        for idx, val in enumerate(nums):
            if val >= 0:
                return idx+1

        return 1 if min_num > 1 else max_num + 1