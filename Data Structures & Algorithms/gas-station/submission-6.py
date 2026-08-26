"""

We need to loop around and end up at the same index
We can only start at indices where cost <= gas

def check(idx):
    curr_gas = gas[curr_idx] - cost[curr_idx]

    i = idx

    while i < (idx+len(gas)-1):
        curr_idx = i % len(gas)

        curr_gas -= cost[idx]

        if curr_gas < 0:
            break

        curr_gas += gas[curr_idx+1] 

        i += 1

    return ((i%len(gas)) == idx)




"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        def check(idx):
            curr_gas = gas[idx]

            i = idx+1

            while i < (idx+len(gas)):
                curr_idx = i % len(gas)

                curr_gas -= cost[curr_idx-1]

                if curr_gas <= 0:
                    break

                curr_gas += gas[curr_idx]

                i += 1

            return bool(i > idx and (i%len(gas)) == idx)

        print(gas[2] >= cost[2], check(2))

        for j in range(len(gas)):
            if gas[j] >= cost[j] and check(j):
                return j

        return -1
        