class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        O(N) Time?

        - We can't sort and count
        - We can use a dict and iterate through - same thing as a set but maintains count?

        - We iterate both forward and backward and remove the numbers as we go on?
            ONLY WORKS BECAUSE WE HAVE EVERYTHING IN THE SET LOADED.
            We end up iterating through every 
        """

        nums_set = set(nums)
        sequence = dict()

        res = 0

        for start_num in nums_set:
            curr_num = start_num
            ctr = 1

            if curr_num-1 not in nums_set:
                curr_num = start_num
                while curr_num+1 in nums_set:
                    ctr += 1
                    curr_num += 1

            res = max(res, ctr)

        return res