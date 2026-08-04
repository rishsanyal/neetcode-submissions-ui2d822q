"""
if no digits:
    we add curr_str to global res
    we return

if digits:
    we get the first one
    we get all characters for it
    we recurse with curr_str and remaining digits
"""



class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        number_mapping = {
            "1": [],
            "2": ["abc"],
            "3": ["def"],
            "4": ["ghi"],
            "5": ["jkl"],
            "6": ["mno"],
            "7": ["pqrs"],
            "8": ["tuv"],
            "9": ["wxyz"]
        }

        res = []


        def r(curr_str, remaining_digits):

            if not remaining_digits:
                if curr_str:
                    res.append(curr_str)
                return
            
            curr_num = remaining_digits[0]

            for chars in number_mapping[curr_num]:
                for c in chars:
                    r(curr_str+c, remaining_digits[1:])

            return


        r("", digits)

        print(res)

        return res