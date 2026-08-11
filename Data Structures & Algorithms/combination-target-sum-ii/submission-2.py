"""
Duplicate combination
[1,2,2,3] - 5
[2,3]
[2,3]

[2, 3]

we sort the list

At each level, we can either use the previous numbers or start a new one
when we start a new list, we start from a new number only

At each level, we either add the number or we don't

If we only start with a unique number, we should get unique results

[1,1,2,3,4,5]

idx+1, sum+num, previous+[num]

"""



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        candidates.sort()

        def r(idx, curr_sum, l):
            if curr_sum == target:
                res.append(l[:])
                return True
            
            if idx >= len(candidates) or curr_sum > target:
                return False

            l.append(candidates[idx])
            r(idx+1, curr_sum+candidates[idx], l)
            l.pop()

            curr_num = candidates[idx]
            while idx < len(candidates)-1 and curr_num == candidates[idx+1]:
                idx += 1

            r(idx+1, curr_sum, l)


        r(0, 0, [])

        print(res)

        return res








        