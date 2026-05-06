class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Calculate the distance for each point from the origin
        and pop min heap
        """
        def __calc(px, py):
            return ((px*px) + (py*py))**(1/2)

        h = [(__calc(p[0], p[1]), p) for p in points]
        res = []

        heapq.heapify(h)

        while h and k:
            res.append(heapq.heappop(h)[1])
            k -= 1

        return res

            
            
