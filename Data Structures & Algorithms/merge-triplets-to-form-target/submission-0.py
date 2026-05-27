"""
We don't do it on all of them
what we could do here is go through each and check fi they're lte and THEN merge
"""

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        curr_triplet = [0, 0, 0]

        for (a,b,c) in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                curr_triplet[0] = max(a, curr_triplet[0])
                curr_triplet[1] = max(b, curr_triplet[1])
                curr_triplet[2] = max(c, curr_triplet[2])

        return curr_triplet == target
                
        