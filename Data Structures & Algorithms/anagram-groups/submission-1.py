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
        """

        # Key -> index of word
        # Value -> Dict of characters and their count
        char_counter = defaultdict(lambda: defaultdict(int))
        result = []

        for idx in range(len(strs)):
            for unicode_curr_char in range(ord('a'), ord('z')+1):
                curr_char=chr(unicode_curr_char)
                char_counter[idx][curr_char] = 0

        for idx, word in enumerate(strs):
            for char in word:
                char_counter[idx][char] += 1

        for idx, char_ctr in char_counter.items():
            char_str = ''
            for char, char_count in char_ctr.items():
                char_str += char + str(char_count)

            # could be a new dict or a list
            char_counter[idx] = char_str

        str_found = {}

        for idx, char_str in char_counter.items():
            if char_str in str_found:
                str_found[char_str].append(idx)
            else:
                str_found[char_str] = [idx]

        result = []

        for _, idx_list in str_found.items():
            temp_res = []
            for idx in idx_list:
                temp_res.append(strs[idx])
            
            result.append(temp_res)

        return result