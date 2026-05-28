class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        res = 0
        curr_gas = 0

        for idx in range(len(gas)):
            curr_gas += (gas[idx] - cost[idx])

            if curr_gas < 0:
                res = idx + 1
                curr_gas = 0

        return res