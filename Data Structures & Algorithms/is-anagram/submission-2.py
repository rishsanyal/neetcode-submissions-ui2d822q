class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Anagram conditions:
        1. When the length of the str is the same
        2. When the count of characters is the same

        O(m+n)
        """

        if len(s) != len(t):
            return False

        tracker = {}

        for c in s:
            tracker[c] = tracker.get(c, 0) + 1
        
        for c in t:
            # New character
            if c not in tracker:
                return False

            tracker[c] = tracker.get(c) - 1

            # Pop character if count 0
            if tracker[c] == 0:
                tracker.pop(c)

        return not tracker