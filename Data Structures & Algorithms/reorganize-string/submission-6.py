"""
- We use a heap for this to track 2 characters
- We have a maxHeap by count
- we check if res and len(heap)==1 and heap[0][1] == res[-1]
- we pop char, store it in temp
- pop another one, if possible
- we repopulate both and continue

axyy
y1

yx

y1
a1

yxya

"""

class Solution:
    def reorganizeString(self, s: str) -> str:

        c = Counter(s)
        h = [(char_count, char) for (char, char_count) in c.items()]
        heapq.heapify_max(h)

        res = ''

        while h:
            curr_count, curr_char = heapq.heappop_max(h)
            res += curr_char

            temp_count, temp_char = None, None

            if curr_count - 1 > 0:
                temp_count, temp_char = curr_count-1, curr_char

            if h:
                curr_count, curr_char = heapq.heappop_max(h)
                res += curr_char

                if temp_count and temp_count > 0:
                    heapq.heappush_max(h, (temp_count, temp_char))

                temp_count, temp_char = curr_count-1, curr_char
            else:
                if temp_count:
                    return ""

            if temp_count and temp_count > 0:
                heapq.heappush_max(h, (temp_count, temp_char))

        return res

                
            


