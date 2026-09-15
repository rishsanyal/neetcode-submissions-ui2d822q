class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        h = [(char_count, char) for (char, char_count) in c.items()]
        heapq.heapify_max(h)

        res = ''

        while h:
            temp = []

            if len(res) >= 2 and res[-1] == res[-2]:
                return ''

            for _ in range(2):
                if h:
                    count, char = heapq.heappop_max(h)

                    res += char

                    if count - 1 > 0:
                        temp.append((count-1, char))

            for i in temp:
                heapq.heappush_max(h, i)

        if len(res) >= 2 and res[-1] == res[-2]:
            return ''

        return res
