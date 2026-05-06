class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        we create a min heap and pop until the list == k and return the first element
        """

        import heapq

        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]