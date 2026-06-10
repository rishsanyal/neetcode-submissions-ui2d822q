"""

- start by sorting the candidates
- for each candidate we can only pick it once
    - on each step we pick a candidate
        we iterate from the index after that
    - on each step we pop a candidate

track - idx, curr_candidates
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def r(idx=0, curr_candidates=[], curr_candidates_sum=0):
            # print(curr_candidates, curr_candidates_sum)
            if curr_candidates_sum == target:
                res.append(curr_candidates[:])
                return

            if idx >= len(candidates) or curr_candidates_sum > target:
                return

            # We have to use both
            curr_candidates.append(candidates[idx])
            r(idx+1, curr_candidates, curr_candidates_sum + candidates[idx])
            curr_candidates.pop()

            while (idx+1 < len(candidates) )and candidates[idx] == candidates[idx+1]:
                idx += 1

            r(idx+1, curr_candidates, curr_candidates_sum)

            return

        r()

        return res
