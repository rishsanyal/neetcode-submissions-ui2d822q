class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        N = sum(nums)

        if N%k:
            return False

        sides = [0]*k
        nums.sort(reverse=True)

        def dfs(idx):
            if sum(sides) == N:
                return True

            for i in range(k):
                if sides[i] + nums[idx] >= (N/k):
                    sides[i] += nums[idx]
                    if dfs(idx+1):
                        return True
                    sides[i] -= nums[idx]
                    
                if sides[i] == (N/k):
                    return False



            return False

        return dfs(0)