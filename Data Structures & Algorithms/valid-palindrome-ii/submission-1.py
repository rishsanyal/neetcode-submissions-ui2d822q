class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        We can at most delete one
        How do we decide which one?
            We delete both and check
            At the first mismatch, we can start checking from there
        """


        def check(inp_str, removed=False):
            print(inp_str)
            l, r = 0, len(inp_str)-1

            if not inp_str:
                return True

            while l < r:
                if inp_str[l] != inp_str[r]:
                    if not removed:
                        return check(inp_str[l:r+1], True) or check(inp_str[l+1:r], True)
                    else:
                        return False
                
                l += 1
                r -= 1

            return True


        return check(s)