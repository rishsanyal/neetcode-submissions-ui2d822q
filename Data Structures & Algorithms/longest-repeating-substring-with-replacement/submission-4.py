"""
We can use a dict to track count but at every point
we can't be gredy because that might backfire

AABBB - 5 without greedy

- You have to maintain a temporary dictionary with a pointer l = 0
- You’re given K where K is the number of operations you can perform on the list
- As you iterate through the list, you have to update the dictionary
- You then check if the size of the list from l to r minus the value of the max key in the dictionary (the most occurring character so far) is less than k
    - This means that you’ll need to do more than K operations to get the string converted to a single character
    - If so, you have to make the window smaller, by moving l closer (l += 1)
    - Don’t  for get to remove it from he dictionary then since our Dict needs to capture rolling information

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        tracker = Counter()

        l, r = 0, 0
        curr_max_num, curr_max_char = 0, None

        res = 0

        for r in range(len(s)):
            curr_char = s[r]
            tracker[curr_char] += 1

            max_val = max(tracker.values())

            while (r - l - max_val + 1) > k:
                tracker[s[l]] -= 1
                max_val = max(tracker.values())
                l += 1

            res = max(res, r-l+1)

        return res
            




        