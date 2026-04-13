class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_dict = {}

        for idx, i in enumerate(nums):
            # print(idx, i)
            if target - i in n_dict:
                return [n_dict[target - i], idx]

            n_dict[i] = idx

        return [-1, -1]