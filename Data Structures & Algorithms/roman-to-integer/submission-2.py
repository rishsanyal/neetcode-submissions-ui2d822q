class Solution:
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """

        roman_single_dict = {
            "I":             1,
            "V":             5,
            "X":             10,
            "L":             50,
            "C":             100,
            "D":             500,
            "M":             1000
        }

        curr_idx = 0
        res = 0
        
        while curr_idx < len(s):
            if curr_idx == len(s)-1:
                res += roman_single_dict[s[curr_idx]]
            else:
                if roman_single_dict[s[curr_idx]] >= roman_single_dict[s[curr_idx+1]]:
                    res += roman_single_dict[s[curr_idx]]
                else:
                    res -= roman_single_dict[s[curr_idx]]

            curr_idx += 1
            
        return res

