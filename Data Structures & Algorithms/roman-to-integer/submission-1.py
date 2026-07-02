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

        roman_double_dict = {
            "IV":           4,
            "IX":           9,
            "XL":           40,
            "XC":           90,
            "CD":           400,
            "CM":           900
        }

        currCounter = 0
        currSum = 0
        
        while currCounter < len(s):
            if s[currCounter: currCounter+2] in roman_double_dict:
                currSum += roman_double_dict[s[currCounter: currCounter+2]]
                currCounter += 2
                continue
            
            if s[currCounter] in roman_single_dict:
                currSum += roman_single_dict[s[currCounter]]
                currCounter += 1
                continue
            

        return currSum

