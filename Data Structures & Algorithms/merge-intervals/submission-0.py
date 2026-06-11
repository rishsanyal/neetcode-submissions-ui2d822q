"""
- we sort since they can be in any order
- we create a new list and append to it 
    if it's empty or if the new interval doesn't intersect with the previous interval in res


[[1,3],[1,5],[6,7]]
[[1,5], [6,7]]

Assuming ideal intervals - start_time <= end_time
all positive, etc

is it okay to run the code?
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals.sort(key=lambda x: x[0])

        for (curr_start, curr_end) in intervals:
            if not res:
                res.append([curr_start, curr_end])
                continue

            prev_start, prev_end = res[-1]

            intersecting = (prev_start <= curr_start <= prev_end) or\
                (prev_start <= curr_end <= prev_end) or\
                (curr_start <= prev_start <= curr_end) or\
                (curr_start <= prev_end <= curr_end)

            if intersecting:
                res[-1] = [
                    min(prev_start, curr_start),
                    max(prev_end, curr_end)
                ]
            else:
                res.append([curr_start, curr_end])

        # print(res)

        return res
            



        



