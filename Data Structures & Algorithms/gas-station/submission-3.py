"""
We can start at the first station where gas[i] >= cost[i]
we iterate from that index (idx) until idx + len(list)
on every index we do the math
gas - cost = 3
4 - 2 = 2
4 - 2 = 2
5 - 4 = 1
we reach the final point


gas = [1,2,3], cost = [2,3,2]

curr_gas = 3
3 - 2 = 1
curr_gas = 1 + 1 = 2

curr_gas = 2 - 2 = 0
0 + 2 = 2
Fail because 2 - 3 < 0
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(cost) > sum(gas):
            return -1

        curr_gas_idx = 0
        ans = True

        for i in range(len(gas)):
            if cost[i] < gas[i]:
                curr_gas_idx = i
                curr_gas = 0

                for j in range(curr_gas_idx, curr_gas_idx+len(gas)+1):
                    idx = ((j) % (len(gas)))
                    curr_gas += gas[idx] - cost[idx]
                    if curr_gas < 0:
                        break

                if curr_gas > 0:
                    break

        return curr_gas_idx if ans else -1