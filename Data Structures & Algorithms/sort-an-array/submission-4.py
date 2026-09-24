class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def __mergesort(inp_list):
            if len(inp_list) == 1:
                return inp_list

            mid = len(inp_list)//2

            left = __mergesort(inp_list[:mid])
            right = __mergesort(inp_list[mid:])

            l, r = 0, 0
            res = []

            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1

            while l < len(left):
                res.append(left[l])
                l += 1

            while r < len(right):
                res.append(right[r])
                r += 1


            return res

        return __mergesort(nums)
