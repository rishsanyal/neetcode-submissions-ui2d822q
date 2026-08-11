# """
# We make a matchstick square with 4 sides of equal length
# - We need to know if the sum % 4 == 0
# - We then want to split the matchsticks into sum / 4 length
#     - selecting mechanism
#         - At each level, we need to add the stick to a side and see if that works
#         - we then remove that stick from that side and move on

#     - as soon as we get a perfect match, we move on



# - Confusing because we need to make a group
# - We could sort and that should build up, right? - Too simple and doesn't work
# - We could use a counter dict and iterate through that? - too weird

# [1,3,4,2,2,4] - 16
# [1,2,2,3,4,4]

# """



# class Solution:
#     def makesquare(self, matchsticks: List[int]) -> bool:
#         if sum(matchsticks) % 4 != 0:
#             return False
#         # N = sum(matchsticks)

#         # if N % 4:
#         #     return False


#         sides = [0]*4
#         matchsticks.sort(reverse=True)

#         def dfs(idx):
#             if idx == len(matchsticks):
#                 return sides[0] == sides[1] == sides[2] == sides[3]

#             for i in range(4):
#                 sides[i] += matchsticks[idx]

#                 if dfs(idx+1):
#                     return True

#                 sides[i] -= matchsticks[idx]

#             return False


#         return dfs(0)
