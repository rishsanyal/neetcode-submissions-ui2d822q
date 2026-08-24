class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen_set = set()

        for i in range(k):
            if nums[i] in seen_set:
                return True

            seen_set.add(nums[i])

        for i in range(k, len(nums)):
            if nums[i] in seen_set:
                return True

            seen_set.remove(nums[i-k])
            seen_set.add(nums[i])

        return False