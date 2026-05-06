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
        """

        c = Counter(s)
        h = [(j,i) for (i,j) in c.items()]
        heapq.heapify_max(h)
        res = ''

        while h:
            temp = []

            if len(res) >= 2 and res[-1] == res[-2]:
                return ""

            for _ in range(2):
                if h:
                    count, char = heapq.heappop_max(h)
                    res += char

                    if count-1:
                        temp.append((count-1, char))

            for i in temp:
                heapq.heappush_max(h, i)

        return res


        

