class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Forgetting the algo's name
        But if we see a number and we treat it as majority until proved otherwise

        0, 0, 0, 1, 2
        """
        
        winner, winner_count = None, 0

        for num in nums:
            if (winner is None) or (winner == num):
                winner = num
                winner_count += 1
            else:
                winner_count -= 1
                if winner_count <= 0:
                    winner_count = 0
                    winner = None

        return winner
