class Solution:
    def mySqrt(self, x: int) -> int:
        """
        - We know that any number between 0 - n is possible to be sqrt
        - We can go to mid - get the square 
            - if it's lower we increase l by mid + 1?
            - elif -> mid = r - 1 or return
        """

        l, r = 0, x

        while l <= r:
            mid = (l+r)//2
            mid_square = mid*mid

            if mid_square == x:
                return mid
            elif mid_square < x:
                l = mid + 1
            else:
                r = mid - 1

        return min(l,r)