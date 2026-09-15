"""
We create a constant 26 character for each word and create a tuple of it
it's constant space and time

that tuple can be the dict key and we group it

sort each word BUT the complexity becomes M*N*lg(N) -> Not necessary



the tuple can be the dict key

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        tracker = defaultdict(list)

        for word in strs:
            tup = [0 for _ in range(27)]
            for curr_char in word:
                tup[ord(curr_char) - ord('a')] += 1

            tracker[tuple(tup)].append(word)

        return ([i for i in tracker.values()])