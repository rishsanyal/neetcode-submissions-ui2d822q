"""
str wise dict
we insert and go on

THINK OF A DELIMETER
BETWEEN PREFIX AND WORD SEARCH
"""


class PrefixTree:

    def __init__(self):
        self.tracker = {}

    def insert(self, word: str) -> None:
        curr_tracker = self.tracker

        for w in word:
            if w not in curr_tracker:
                curr_tracker[w] = {}

            curr_tracker = curr_tracker[w]
        
        curr_tracker["#"] = {}
        

    def search(self, word: str, word_search=True) -> bool:
        curr_tracker = self.tracker

        for w in word:
            if w not in curr_tracker:
                return False
            
            curr_tracker = curr_tracker[w]

        if word_search:
            return ('#' in curr_tracker)
        else:
            return True
    
        
    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, False)
        