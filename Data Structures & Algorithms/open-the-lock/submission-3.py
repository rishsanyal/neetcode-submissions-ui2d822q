class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        It's a type of BFS since we need the MINIMUM number of turns to open the lock.

        for each number we start with [0,0,0,0]
        we increase one number and track previous numbers in a visited set.

        we keep going until we hit a visited number, a deadend or the target

        we track the curr number + num of turns in the BFS deque
        """

        tracker = deque()
        tracker.append(([0,0,0,0], 0))
        visited = set()
        res = -1

        deadends = set(deadends)

        while tracker:
            curr_num, curr_turns = tracker.popleft()

            curr_num_str = ''.join([str(i) for i in curr_num])

            if curr_num_str in deadends or curr_num_str in visited:
                continue

            if curr_num_str == target:
                return curr_turns

            visited.add(curr_num_str)

            for i in range(4):
                # Not sure if copying like this works, let's test that.
                new_num = curr_num.copy()
                new_num[i] = (new_num[i]+1)%10

                tracker.append((new_num, curr_turns+1))

            for i in range(4):
                # Not sure if copying like this works, let's test that.
                new_num = curr_num.copy()
                new_num[i] = (new_num[i]-1)%10

                tracker.append((new_num, curr_turns+1))

        
        return res

