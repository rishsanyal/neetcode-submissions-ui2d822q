"""
Hoping nobody's weight is above the limit already

most - right pointer
least - left pointer

We sort the people
we add the least + most
if that's too much, we only send the most
keep going until l <= r
"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people)-1
        res = 0

        people.sort()

        while l <= r:
            curr_boat = people[l] + people[r]

            if people[l] + people[r] > limit:
                r -= 1
            else:
                l += 1
                r -= 1
    
            res += 1

        return res
