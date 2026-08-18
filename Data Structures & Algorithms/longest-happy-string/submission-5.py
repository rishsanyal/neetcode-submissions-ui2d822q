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

        h = [
            (a, 'a'),
            (b, 'b'),
            (c, 'c')
        ]
        heapq.heapify_max(h)

        prev_char, prev_count = '', 0

        res = ''

        while h:
            curr_count, curr_char = heapq.heappop_max(h)

            if curr_count == 0:
                continue
            
            if curr_count >= 2:
                res += (curr_char*2)
                curr_count -= 2
            elif curr_count == 1:
                res += curr_char
                curr_count -= 1

            if (prev_count > 0):
                heapq.heappush_max(
                    h,
                    (prev_count, prev_char)
                )
            
            prev_char, prev_count = curr_char, curr_count

        return res

            





        