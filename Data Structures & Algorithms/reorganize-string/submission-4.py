class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        We could insert every character in a counter dict and loop through the dict
        we'd need to sort the counter first

        if the last 2 chars are same, we exit?

        axyy ->
        y:2
        x:1
        a:1

        yxay


        xxxxd:
        x:4
        d:1
        xdxx -> -1

        abbccdd
        d-2
        c-2
        b-2
        a-1

        dcbadcb

        Sort by freq?

        But we JUST care about the previous char
        """

        c = Counter(s)
        h = [(j,i) for (i,j) in c.items()]
        heapq.heapify_max(h)
        res = ''

        prev = None

        while h or prev:
            if prev and not h:
                return ""

            count, char = heapq.heappop_max(h)
            res += char

            if prev:
                heapq.heappush_max(h, prev)

            if count-1:
                prev = (count-1, char)
            else:
                prev = None

        return res
            


        

