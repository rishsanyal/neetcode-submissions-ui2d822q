"""

- We track the number of bills we have in a dict
- We could be greedy and return the big bills

{5: 0, 10: 0, 20: 0}

for bill in bills:

    change = bill - 5

    # 5
    if change == 0:
        tracker[bill] += 1
        continue

    # 10
    if change == 5:
        if tracker[5] >= 1:
            tracker[bill] += 1
            continue
        else:
            return False

    # 20
    if change == 15:
        if tracker[5] >= 1 and tracker[10] >= 1:
            tracker[bill] += 1
            continue
        else:
            return False

return True

            

"""



class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        tracker = {5: 0, 10: 0, 20: 0}

        for bill in bills:

            change = bill - 5

            # 5
            if change == 0:
                tracker[bill] += 1
                continue

            # 10
            if change == 5:
                if tracker[5] >= 1:
                    tracker[bill] += 1
                    continue
                else:
                    return False

            # 20
            if change == 15:
                if tracker[5] >= 1 and tracker[10] >= 1:
                    tracker[bill] += 1
                    continue
                else:
                    return False

        return True
