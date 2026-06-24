class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        captial, profits

        we need min capital and max profits
        k projects and w working capital

        we take capital projects out until we can afford it
        put it in a max heap by (profits)
        pop the top one
        gain the additional capital and repeat
        """

        working_capital = w

        capital_min_heap = [(capital[i], profits[i]) for i in range(len(profits))]
        heapq.heapify(capital_min_heap)

        can_afford = capital_min_heap[0][0] <= working_capital

        profit_max_heap = []

        while (can_afford or profit_max_heap) and k:
            print(working_capital)

            # We take out all projects we can afford
            while capital_min_heap and capital_min_heap[0][0] <= working_capital:
                curr_capital, curr_profit = heapq.heappop(capital_min_heap)
                heapq.heappush_max(profit_max_heap, (curr_profit, curr_capital))

            # Can't afford any project
            if not profit_max_heap:
                break

            # print(profit_max_heap)

            working_capital += heapq.heappop_max(profit_max_heap)[0]

            # print(working_capital)

            can_afford = (capital_min_heap and (capital_min_heap[0][0] <= working_capital))

            k -= 1

        return working_capital

        



            






