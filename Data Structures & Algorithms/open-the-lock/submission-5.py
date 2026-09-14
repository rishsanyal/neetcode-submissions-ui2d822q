"""
- Numbers can go up or down on the wheel
- We need the minimum number of turns for this (bfs because we need to find the first path)

- We start with 0,0,0,0 - could be a tuple that we adjust (easier)
- we change each wheel (+1, -1) % 9 and pass to the bfs algo
- visited nodes? we should track them since it's possible
    - setof tuples since tuples are hashable
"""

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def bfs():
            start_num = [0, 0, 0, 0]
            q = deque([(start_num, 0)])

            visited = set()

            while q:
                (curr_num, curr_steps) = q.popleft()
                curr_combo = str(curr_num[0])+str(curr_num[1])+str(curr_num[2])+str(curr_num[3])

                if curr_combo in visited or curr_combo in deadends:
                    continue

                if curr_combo == target:
                    return curr_steps

                for idx, num in enumerate(curr_num):
                    for i in (1, -1):
                        new_num = curr_num[:idx] + [(num+i)%10] + curr_num[idx+1:]
                        q.append((new_num, curr_steps+1))

                visited.add(curr_combo)

            return -1

        return bfs()

                    


