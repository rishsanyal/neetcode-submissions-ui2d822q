class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Forgetting the algo's name
        But if we see a number and we treat it as majority until proved otherwise

        3, 3, 4, 4, 3
        """
        
        winner, winner_count = None, 0

        for num in nums:
            if not winner or winner == num:
                winner = num
                winner_count += 1
            else:
                winner_count -= 1
                if winner_count <= 0:
                    winner_count = 0
                    winner = num

        return winner
