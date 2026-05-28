"""
We have a list

We check which number is optimal
if equal, we get the max

if alice's turn, we add the number to her score, else we add it to bob's



"""

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        total = sum(piles)
        q = piles

        def r(alice_score, turn, left_idx, right_idx):
            if left_idx == right_idx:
                return alice_score

            if (left_idx, right_idx, turn) in cache:
                return cache[(left_idx, right_idx, turn)]

            res = 0

            if q[left_idx] > q[right_idx]:
                if turn:
                    res = r(q[left_idx] + alice_score, not turn, left_idx+1, right_idx)
                else:
                    res = r(alice_score, not turn, left_idx+1, right_idx)
            elif q[left_idx] < q[right_idx]:
                if turn:
                    res = r(q[right_idx] + alice_score, not turn, left_idx, right_idx-1)
                else:
                    res = r(alice_score, not turn, left_idx, right_idx-1)
            else:
                if turn:
                    res = max(r(q[left_idx] + alice_score, not turn, left_idx+1, right_idx), r(q[left_idx] + alice_score, not turn, left_idx, right_idx-1))
                else:
                    res = max(r(alice_score, not turn, left_idx+1, right_idx), r(alice_score, not turn, left_idx, right_idx-1))

            cache[(left_idx, right_idx, turn)] = res

            return cache[(left_idx, right_idx, turn)]

        alice_score = r(0, True, 0, len(piles)-1)

        print(alice_score)

        return alice_score > (total-alice_score)



            



