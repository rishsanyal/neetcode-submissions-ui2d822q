class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """

        trips.sort(key=lambda x: x[1])
        
        h = []
        curr_cap = 0

        for (cap, start, end) in trips:
            while h and start >= h[0][0]:
                _, prev_cap = heapq.heappop(h)
                curr_cap -= prev_cap
            
            curr_cap += cap

            if curr_cap > capacity:
                return False

            heapq.heappush(h, (end, cap))

        return True