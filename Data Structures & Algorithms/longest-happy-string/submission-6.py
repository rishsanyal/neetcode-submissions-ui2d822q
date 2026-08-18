"""
- we could pop from a max heap
- we pop 2 at a time and make sure we only populate when heap's empty?
- we just need to track the last one

we track prev count and previous char
a = 0, b = 0, c = 5

[(5,c), (1,b)]

cc
c,3
[(1,b)]

ccb
b,0
[(3, c)]

ccbcc
c,1
[]


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

        prev_char, prev_count = '', 0

        res = ''

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

            





        