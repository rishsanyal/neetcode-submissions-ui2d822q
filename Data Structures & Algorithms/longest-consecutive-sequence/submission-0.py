class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        O(N) Time?

        - We can't sort and count
        - We can use a dict and iterate through - same thing as a set but maintains count?

        [0,3,2,5,4,6,1,1]

        {
            0: 1
            1: 2
            2: 3
            3: 4
            4: 5
            5: 6
            6: 7
        }

        Could be N^2, if we iterate from every number forward?
        Should be O(N) if we go backward? NO because we'd still go N^2

        We do iterate after inserting everything
        So we maintain a visited set and don't re-visit numbers

        We put everything in a set
        we can maintain a dict with previous length too
        check in set:
            if not in set and not in dict -> 1
            if not in set and in dict -> 1 + dict.get(number)
            if in set (can't be in dict)
        iterate through the dict for the longest answer

        [0,3,2,5,4,6,1,1]

        {2, 3, 4, 5, 6}
        {
            0: 1,
            1: 2,
            2: 3,
            4: 4
        }

        What if we just put everything in a dict and modify it as we go on? - maybe?
        """

        nums_set = set(nums)
        sequence = dict()

        res = 0

        while nums_set:
            curr_num = nums_set.pop()

            ctr = 1
            if curr_num not in sequence:
                prev_num = curr_num-1

                if prev_num in sequence:
                    ctr += sequence[prev_num]

            sequence[curr_num] = ctr
            res = max(res, ctr)

        return res

        






