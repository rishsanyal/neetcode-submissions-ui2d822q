class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Merge Sort
        - Pick a pivot
        - split the list around it
        - merge it

        can we do it in place?
        """

        def mergesort(inp):
            pivot = (0 + len(inp)) // 2
            lt, gt, eq = [], [], []

            if not inp or len(inp) == 1:
                return inp

            for num in inp:
                if num < inp[pivot]:
                    lt.append(num)
                elif num == inp[pivot]:
                    eq.append(num)
                else:
                    gt.append(num)

            return mergesort(lt) + eq + mergesort(gt)

        return mergesort(nums)

                
                

