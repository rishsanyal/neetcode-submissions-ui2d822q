class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergesort(inp_arr):
            n = len(inp_arr)
            if n <= 1:
                return inp_arr


            mid = n // 2
            left = mergesort(inp_arr[:mid])
            right =  mergesort(inp_arr[mid:])

            res = []

            i,j = 0, 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            res += left[i:]
            res += right[j:]

            return res

        return(mergesort(nums))
