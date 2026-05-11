class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        We have the min and the max

        let's assume valid cases
        Should be in the realm of set-iteration

        iterate through, find the min and the max
        keep iterating from the min to go and find the max
        """

        min_num, max_num = min(nums), max(nums)

        nums = set(nums)

        min_num = max(0, min_num)

        for num_to_check in range(min_num, max_num+2):
            if num_to_check not in nums:
                return num_to_check

        return 1

