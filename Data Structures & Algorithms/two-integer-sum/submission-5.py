class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for (idx,num) in enumerate(nums):

            if (target - num) in tracker:
                if idx < tracker[target-num]:
                    return [idx, tracker[target-num]]
                else:
                    return [tracker[target-num], idx]

            tracker[num] = idx

        return []
