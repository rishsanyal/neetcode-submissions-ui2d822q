class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        abs(i-j)<=k is the hint here

        we go from 0 to k

        we maintain a small hash dict
        we remove - on every iteration and we add one on every iteration

        if the number exists, we check and return
        """
        ctr = {}

        idx = 0

        for i in range(0, len(nums)):
            if nums[i] in ctr:
                return True

            ctr[nums[i]] = i

            if len(ctr) == k+1:
                ctr.pop(nums[idx])
                idx += 1

        return False

            

        



