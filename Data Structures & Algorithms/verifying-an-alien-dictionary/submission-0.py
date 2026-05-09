class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        Feel like we can use a custom priortiy queue for this.

        custom sorting -> custom character class with operators overloaded

        we can keep iterating through the words and pop characters off it to compare against the previous character
        """

        order_index = {c: i for i, c in enumerate(order)}
        def compare(word):
            return [order_index[c] for c in word]

        return words == sorted(words, key=compare)