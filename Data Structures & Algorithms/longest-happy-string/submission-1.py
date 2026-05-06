class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        at most 2 characters can be togehter
        """

        prev=None
        h=[(a,'a'), (b,'b'), (c, 'c')]
        heapq.heapify_max(h)

        res = ""

        while h or prev:
            if prev and not h:
                # We'll only enter this case if we have 1 char 
                # remaining
                return res

            
            count, char = heapq.heappop_max(h)

            if count == 0:
                continue

            if count > 2:
                res += char*2
                count -= 2
            else:
                res += char
                count -= 1

            if prev:
                heapq.heappush_max(h, prev)
                prev = None

            if count:
                prev = (count, char)
            else:
                prev = None

        return res
            

            

            