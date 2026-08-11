"""

- We can delete AT MOST 1 character (0-1)
- We'd only delete the character in case something doesn't match (use a bool)
- we'd have 2 pointers and if there's a mismatch we'd use the boolean

"""



class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s)-1
        deleted = False

        def check(l, r):
            nonlocal deleted

            if l > r:
                return False
            
            while l <= r:
                if s[l] != s[r]:
                    if deleted:
                        return False
                    
                    deleted = True
                    return check(l, r-1) or check(l+1, r-1)

                l += 1
                r -= 1

            return True

        return check(l, r)
