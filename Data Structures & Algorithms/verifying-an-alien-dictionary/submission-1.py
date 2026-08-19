class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_dict = {}

        for idx, i in enumerate(order):
            order_dict[i]=idx

        def compare(word):
            return [order_dict[i] for i in word]

        return words == sorted(words, key=compare)