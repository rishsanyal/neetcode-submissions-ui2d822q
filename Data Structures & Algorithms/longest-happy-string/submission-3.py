"""
There can't be more than 2 characters joined in
only a,b and c
we know the count of a, b and c
return "" if not possible

Greedy
use a heap to track
- a = 3, b = 4, c = 2
aabbccbba

- a = 4, b = 0, c = 0
aaaa - Not possible

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

        prev_char = None

        res = ''
        temp_char, temp_count= '', 0

        while h:
            count, char = heapq.heappop_max(h)

            if char == prev_char:
                temp_char, temp_count = char, count

                if h:
                    count, char = heapq.heappop_max(h)
                else:
                    return res

            if count == 1:
                res += char
                count -= 1
            elif count >= 2:
                res += char*2
                count -= 2

            if count > 0:
                prev_char = char
            else:
                prev_char = None

            if temp_char:
                if temp_count == 1:
                    res += temp_char
                    temp_count -= 1
                elif temp_count >= 2:
                    res += temp_char*2
                    temp_count -= 2

                if temp_count > 0:
                    prev_char = temp_char
                else:
                    prev_char = None

            if count > 0:
                heapq.heappush_max(h, (count, char))

            if temp_count > 0:
                heapq.heappush_max(h, (temp_count, temp_char))
                temp_char, temp_count = '', 0
        
        return res





                







        