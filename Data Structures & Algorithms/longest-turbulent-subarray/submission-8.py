"""
we need to track the status and prev number?

there's 2 ways of being turbulent

a > b < c
or 
a < b > c

we take the first 2 numbers
check which way the turbulence goes
increase counter until it's the same way

reset counter

if len < 2:
    return len(arr)

if len == 2:
    return 2 if [arr[0] != arr[1]]

a, b = arr[0], arr[1]
lt = (a > b)

curr_res = 0
res = 2 if (a != b) else 1

break = False

for num in arr[2:]:
    curr_num = num

    if (curr_num > b and not lt) or (curr_num < b and lt):
        curr_res += 1
        next_num_greater = not next_num_greater
    else:
        break = True

    if break:
        res = max(curr_res, res)
        lt = (curr_num > b)

        break = False

    b = curr_num

[2,4,3]
2 < 4 -> lt = True

b        4 3 2
curr_num 3 2 



"""


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        if len(arr) < 2:
            return len(arr)

        if len == 2:
            return 2 if [arr[0] != arr[1]] else 1

        a, b = arr[0], arr[1]
        lt = (a < b)

        curr_res = 2 if (a != b) else 1
        res = curr_res

        reset = False

        for num in arr[2:]:

            curr_num = num

            if (curr_num > b and not lt) or (curr_num < b and lt):
                curr_res += 1
                lt = not lt
            else:
                res = max(curr_res, res)
                lt = (curr_num > b)
                
                curr_res = 1 if curr_num == b else 2

            b = curr_num


        return max(curr_res, res)
                