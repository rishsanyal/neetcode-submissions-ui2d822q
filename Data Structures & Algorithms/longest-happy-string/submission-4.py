"""
There can't be more than 2 characters joined in
only a,b and c
we know the count of a, b and c
return "" if not possible

Greedy
use a heap to track
- a = 3, b = 4, c = 2
aabbccbba

- a = 10, b = 2, c = 2
aabaa

So we need to maintain a previous count and character
we swap it after getting the next one from the heap

- maintain a heap with count
- pop 1 item
- add to str
- track the char
- push to heap
- if it's equal to the prev char, pop it, store it, pop second item and 
- add that to str
- add first char and count to str
- repush both


TIP: ADD ONE AT A TIME

"""

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = []

        if a:
            h.append((a, 'a'))
        if b:
            h.append((b, 'b'))
        if c:
            h.append((c, 'c'))

        heapq.heapify_max(h)

        prev_char, prev_count = None, 0

        res = ''
        temp_char, temp_count= '', 0


        while h:
            # If the prev char == top of the heap, pop 2
            # else pop 1

            count, char = heapq.heappop_max(h)

            if len(res) > 1 and res[-1] == res[-2] == char:
                if h:
                    new_count, new_char = heapq.heappop_max(h)
                else:
                    return res

                res += new_char
                new_count -= 1

                if new_count > 0:
                    heapq.heappush_max(h, (new_count, new_char))

            else:
                res += char
                count -= 1

            if count > 0:
                heapq.heappush_max(h, (count, char))

        return res



















