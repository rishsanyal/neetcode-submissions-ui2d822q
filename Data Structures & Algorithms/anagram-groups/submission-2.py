class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Anagram:
        - Same length
        - Same characters in different order

        One way is that we sort them and compare

        MN*Lg(N)

        or we could have a hashmap of each word of each character
        If the hashmap is the same we group them together

        For every character of every word (longest string)
        we compare every character of every word

        We could encode every alphabet in order and it's occurances
        27*N
    
        For every word, we compare the string to the previously gotten one

        1. We create a dict for every word, keyed by word index and the values will be dict from a-z with their count
        2. For the dict for each word, make a string with the count. Dict preserves insertion order, so we should be good here
        3. Group by sorted string

        We could do all of this in one shot??

        - Go through each word, each character, count the string and use a dict
        """

        tracker = defaultdict(list)
        char_dict = {chr(char): 0 for char in range(ord('a'), ord('z')+1)}

        for word in strs:
            # Make a static char dict
            curr_char_counter = char_dict.copy()
            
            for char in word:
                curr_char_counter[char] += 1

            tracker_key = ''
            for k,v in curr_char_counter.items():
                tracker_key += k + str(v)

            tracker[tracker_key].append(word)

        return list(tracker.values())
