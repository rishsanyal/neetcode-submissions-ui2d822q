"""

We add in reverse
We add 1 to the last digit
we track if there's a 1 to be carried
if so, we add 1 to the previous number and reset the tracker (bool)
and so on

in the end, if the bool is still True, we add 1 to the list


[1,2,3,4]

4 -> 5


"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        add_one = True

        for idx in range(len(digits)-1, -1, -1):
            curr_num = digits[idx]

            if add_one:
                curr_num += 1
                digits[idx] = curr_num % 10
                add_one = curr_num >= 10
            else:
                continue


        if add_one:
            digits.insert(0, 1)

        return digits


        

