class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def quicksort(left, right):
            if left < right:
                pivot = partition(left, right)
                quicksort(left, pivot-1)
                quicksort(pivot+1, right)
        
        def partition(left, right):
            i, j = left, right-1
            pivot = right

            while i < j:
                while (nums[i] <= nums[pivot]) and (i < right):
                    i += 1
                while (nums[j] >= nums[pivot]) and (j > left):
                    j -= 1

                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]

            if nums[pivot] < nums[i]:
                nums[i], nums[pivot] = nums[pivot], nums[i]

            return i

        quicksort(0, len(nums)-1)