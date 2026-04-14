class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(left, right):
            if left < right:
                pivot = partition(left, right)
                quicksort(left, pivot-1)
                quicksort(pivot+1, right)

        def partition(low, high):
            i = low
            j = high - 1
            pivot = high

            while i < j:
                while (nums[i] <= nums[pivot]) and (i < high):
                    i += 1
                while (nums[j] >= nums[pivot]) and (j > low):
                    j -= 1

                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]

            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]

            return i


        quicksort(0, len(nums)-1)

        return(nums)