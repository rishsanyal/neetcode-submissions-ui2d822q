"""

We insert words in a dict
{}
{
    's': {
        'a': {
            'y': {
                '#': {}
            }
        }
    }
}


If we see a '.', we have to loop through all the options 

"""

class WordDictionary:

    def __init__(self):
        self.tracker = {}

    def addWord(self, word: str) -> None:
        curr_tracker = self.tracker
        for w in word:
            if w not in curr_tracker:
                curr_tracker[w] = {}
            curr_tracker = curr_tracker[w]

        curr_tracker['#'] = {}
        
    def search(self, word: str, curr_tracker=None) -> bool:
        if curr_tracker is None:
            curr_tracker = self.tracker

        if not word:
            return '#' in curr_tracker

        for idx, w in enumerate(word):
            if w == '.':
                # loop through all the characters in curr_tracker
                for char, new_tracker in curr_tracker.items():
                    res = self.search(word[idx+1:], new_tracker)

                    if res:
                        return True

                return False
            else:
                if w not in curr_tracker:
                    return False
                curr_tracker = curr_tracker[w]

        return '#' in curr_tracker


