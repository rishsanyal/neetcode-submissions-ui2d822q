class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            while l < len(s) and (not s[l].isalpha()):
                l += 1

            while r >= 0 and (not s[r].isalpha()):
                r -= 1

            if not ((0 <= l < len(s)) and (0 <= r < len(s))):
                return False

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1


        return True


