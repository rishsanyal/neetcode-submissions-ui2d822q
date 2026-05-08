class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
            Water can flow into a neighbor if height equal or lower.

            Water flows in from the oceans into the cells

            We need to find the cell from which water can flow into both oceans.

            So we could go backwards -> from the ocean go to cells that are higher
            maintain a visited set of row,column tuples
            do a set intersection in the end

            Do a BFS from each ocean into all the cells water can flow into
            Add that to a set for the ocean

            do a intersection of the 2 oceans
            The common ones will flow into both oceans
        """

        atlantic_deque, pacific_deque = deque(), deque()
        pacific_set, atlantic_set = set(), set()

        neighbors = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        # Get the starting points of each ocean

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0 or c == 0:
                    pacific_deque.append((r,c))
                if r == len(heights)-1 or c == len(heights[0])-1:
                    atlantic_deque.append((r,c))

        while atlantic_deque:
            r, c = atlantic_deque.popleft()

            # # OOB
            # if not (0 <= r < len(heights)) or not (0 <= c < len(heights[0])):
            #     continue

            # visited
            if ((r, c)) in atlantic_set:
                continue

            atlantic_set.add((r, c))

            for dr, dc in neighbors:
                if (0 <= dr+r < len(heights)) and (0 <= dc+c < len(heights[0])) and heights[dr+r][dc+c] >= heights[r][c]:
                    atlantic_deque.append((dr+r, dc+c))


        while pacific_deque:
            r, c = pacific_deque.popleft()

            # # OOB
            # if not (0 <= r < len(heights)) or not (0 <= c < len(heights[0])):
            #     continue

            # visited
            if ((r, c)) in pacific_set:
                continue

            pacific_set.add((r, c))

            for dr, dc in neighbors:
                if (0 <= dr+r < len(heights)) and (0 <= dc+c < len(heights[0])) and heights[dr+r][dc+c] >= heights[r][c]:
                    pacific_deque.append((dr+r, dc+c))


        return(list(pacific_set & atlantic_set))


            

            

        

