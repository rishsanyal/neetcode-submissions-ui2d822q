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

        print(candidates)

        res = []

        def r(idx=0, curr_candidates=[], curr_candidates_sum=0):
            # print(curr_candidates, curr_candidates_sum)
            if curr_candidates_sum == target:
                res.append(curr_candidates)
                return

            if idx >= len(candidates) or curr_candidates_sum > target:
                return

            for new_idx in range(idx, len(candidates)):
                r(new_idx+1, curr_candidates + [candidates[new_idx]], curr_candidates_sum + candidates[new_idx])

            return

        r()

        return res



        