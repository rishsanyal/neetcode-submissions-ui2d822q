
"""
- 2 pointer approach because we have a hint of 2 people
- we sort the list
- l, r = 0, len(people)-1

while l < r:
    if people[l] + people[r] > limit:
        put people[r] on the boat
        r -= 1
    else:
        put both on boat
        l += 1
        r -= 1


[1,3,2,3,2]

[1,2,2,3,3] - LIMIT=3
[1,2,2,3], 1
[1,2,2], 2
[2], 3
[] 4


[5,1,4,2] - LIMIT - 6
[1,2,4,5]

[2,4], [1,5] - 2
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        res = 0
        people.sort()

        l, r = 0, len(people)-1

        while l < r:
            curr_sum = people[l] + people[r]

            if curr_sum > limit:
                res += 1
                r -= 1
            else:
                res += 1
                l += 1
                r -= 1

        return res + 1 if l == r else res












        