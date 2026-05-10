class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """

        There can only be 2 numbers
        We start a count per element
        if it reaches above n//3 then we add it to the list
        but if it doesn't then what?

        [1,2,1,3,2,3,1,2]

        we maintain 2 trackers
        we start counting
        if a new number comes, do we attack a single number or both? - both

        a new number comes in, both take a hit and are set to none

        we iterate
        if either is set to None, we replace and set the count to 1

        if a new number comes
            if it's n1 or n2 we increase count
            if it's new
                we -1 from n1_count and n2_count and if either of them are >=0, we reset to the number destroying them

        at the end if any of them have a count >= 1, we add that to the answer

        We need to destroy the one with the lesser count
        [5,4,2,3,1,1] -> [1]

        1, None

        [5,2,3,2,2,2,2,5,5,5]

        [1,2,3]

        [3,2,3]
        
        
        """

        n1, n2 = None, None
        n1_count, n2_count = 0, 0

        for num in nums:
            if num == n1:
                n1_count += 1
            elif num == n2:
                n2_count += 1
            else:
                if not n1:
                    n1 = num
                    n1_count = 1
                elif not n2:
                    n2 = num
                    n2_count = 1
                else:
                    n2_count -= 1
                    n1_count -= 1

                    # if n2_count == 0 and n1_count == 0:
                    #     n2 = None
                    #     n1 = None
                    # elif n2_count == 0:
                    #     n2_count = 0
                    #     n2 = None
                    # elif n1_count == 0:
                    #     n1_count = 0
                    #     n1 = None


                    if n2_count <= 0:
                        n2_count = 1
                        n2 = num
                    elif n1_count <= 0:
                        n1_count = 1
                        n1 = num

            if n1_count < n2_count:
                n1, n1_count, n2, n2_count = n2, n2_count, n1, n1_count

        res = []

        n1_count, n2_count = 0, 0

        for num in nums:
            if num == n1:
                n1_count += 1
            elif num == n2:
                n2_count += 1


        if n1_count > len(nums)//3:
            res += [n1]
        if n2_count > len(nums)//3:
            res += [n2]

        return res









