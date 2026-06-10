
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total%k:
            return False

        nums.sort(reverse=True)
        partition_limit = total // k
        used = [False] * len(nums)

        def r(idx, num_partitions, curr_sum):
            if num_partitions == 0:
                return True
            
            if curr_sum == partition_limit:
                return r(0, num_partitions - 1, 0)

            for j in range(idx, len(nums)):
                if (used[j]) or (curr_sum + nums[j]) > partition_limit:
                    continue
                # used.add(j)
                used[j] = True
                if r(j, num_partitions, curr_sum + nums[j]):
                    return True
                # used.remove(j)
                used[j] = False

            return False

        return r(0, k, 0)