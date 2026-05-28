"""
At every point, the choice is between the last index and the first index
they alternate in turns

turn piles into a deque for easy access
- We track turns using a bool 0 for alice, 1 for Bob
- we track the stones using a counter
- while q: pick a pile
- compare at the end

How do we play optimally?
We could do this like a DP question but that becomes n^2 because we'll have to track the idx
- let's do that

def r(total-alice, q, turn):
    we need to track the score right?

cache[len(q), idx_picked] = (curr_alice_sum, curr_bob_sum)
cache[len(q)-1, idxidx_pickedidx_picked] = (curr_alice_sum + r(...), curr_bob_sum)
cache[len(q)-2, idx_picked] = (curr_alice_sum, curr_bob_sum + + r(...))


"""

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        turn = True # 1 for alice
        piles_q = piles

        cache = {}

        def r(q, alice_score, bob_score, turn):
            if not q:
                return (alice_score, bob_score)

            idx_to_choose = not int(turn)
            idx_popped = 0

            if q[-1] > q[0]:
                res = q.pop(-1)
                idx_popped = -1
            elif q[-1] < q[0]:
                res = q.pop(0)
                idx_popped = 0
            else:
                if turn:
                    select_right, select_left = r(q[:-1], q[0] + alice_score, bob_score, not turn), r(q[1:], q[0] + alice_score, bob_score, not turn)
                else:
                    select_right, select_left = r(q[:-1], alice_score, q[0] + bob_score, not turn), r(q[1:], alice_score, q[0] + bob_score, not turn)

                if select_right[idx_to_choose] > select_left[idx_to_choose]:
                    idx_popped = 0
                else:
                    idx_popped = -1

                res = max(select_right[idx_to_choose], select_left[idx_to_choose])

            next_q = q
            if idx_popped == 0:
                next_q = q[1:]
            else:
                next_q = q[:-1]

            if turn:
                return r(next_q, res + alice_score, bob_score, not turn)
            else:
                return r(next_q, alice_score, bob_score + res, not turn)

        a, b = r(piles_q, 0, 0, turn)

        return a > b