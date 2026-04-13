class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        O(N) Solution:
        - Insert in dict
        - Check if target - current number is in dict, if so return the index
        - By the end of the list, we should either have a hit or we don't
        """

        tracker = {}

        for idx, val in enumerate(nums):
            if target-val in tracker:
                return [tracker[target-val], idx]
            
            tracker[val]=idx

        return []

        
        