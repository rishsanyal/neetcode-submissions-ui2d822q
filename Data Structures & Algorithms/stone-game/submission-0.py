"""
At every point, the choice is between the last index and the first index
they alternate in turns

turn piles into a deque for easy access
- We track turns using a bool 0 for alice, 1 for Bob
- we track the stones using a counter
- while q: pick a pile
- compare at the end

"""

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        turn = True # 1 for alice
        q = deque(piles)

        a_ctr, b_ctr = 0, 0

        while q:

            if q[0] >= q[-1]:
                pile = q.popleft()
            elif q[0] < q[-1]:
                pile = q.pop()

            if turn:
                a_ctr += pile
            else:
                b_ctr += pile

            print(turn, pile)
            
            turn = not turn

        return bool(a_ctr > b_ctr)