class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        N = sum(nums)

        if N%k:
            return False


        sides = [0]*k

        def dfs(idx):
            if idx == len(nums):
                return all(side == N/k for side in sides)

            for i in range(k):
                if sides[i] + nums[idx] <= (N/k):
                    sides[i] += nums[idx]
                    if dfs(idx+1):
                        return True
                    sides[i] -= nums[idx]

            return False

        return dfs(0)