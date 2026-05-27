"""
Use BFS
we add every index possible to a queue and check if the last index is visited

0100000000 minJump=2 maxJump=8

"""

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        q = deque()
        q.append(0)

        farthest = 0

        while q:
            curr_idx = q.popleft()
            start = max(curr_idx+minJump, farthest+1)

            if s[curr_idx] == "1":
                continue
            
            if curr_idx == len(s)-1:
                return True

            for i in range(start, curr_idx+maxJump+1):
                if i <= len(s)-1:
                    q.append(i)

            farthest = curr_idx + maxJump
        
        print(farthest)

        return False