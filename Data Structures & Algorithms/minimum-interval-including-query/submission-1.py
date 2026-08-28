"""
We need a way to get the least difference, interval
for each query

queries are unique - so chill

- we sort the queries
- we put all intervals in a min heap by their difference and their end time and their start time

[[1,3],[2,3],[3,7],[6,6]]
[2,3,1,7,6,8]


[1,2,3,6,7,8]

h = [
    (0, 6, 6)
    (1, 3, 2)
    (2, 3, 1)
    (4, 7, 3)
]

[1,2,3,6,7,8]

h = [
    (1, 6, 6)
    (2, 2, 3)
    (3, 1, 3)
    (5, 3, 7)
]

query_dict[query[i]] = result

This way, we just need the first hit
if end time's greater than query, we repopulate for other queries


"""
import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        res = []

        res_final = [-1]*len(queries)

        query_info = [(query_num, idx) for (idx, query_num) in enumerate(queries)]
        query_info.sort(key=lambda x: x[0])

        h = []

        for interval in intervals:
            heapq.heappush(
                h,
                (interval[1] - interval[0]+1, interval[1], interval[0])
            )

        for (query_num, query_idx) in query_info:
            temp = []
            added = False

            while h:
                curr_diff, curr_end, curr_start = heapq.heappop(h)
                intersecting = curr_start <= query_num <= curr_end

                if intersecting:
                    # res.append(curr_diff)
                    res_final[query_idx] = curr_diff
                    temp.append((curr_diff, curr_end, curr_start))
                    added = True

                    break
                else:
                    if curr_end > query_num:
                        temp.append((curr_diff, curr_end, curr_start))

            # if not added:
            #     res.append(-1)
            #     res_final[query_idx] = -1

            while temp:
                heapq.heappush(
                    h,
                    temp.pop()
                )

        # for _, query_idx in query_info:
        #     res_final.append(res[query_idx])

        return res_final





        