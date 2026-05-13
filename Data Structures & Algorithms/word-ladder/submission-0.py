class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        we get all chararacters -> alphabets = string.ascii_lowercase
        for every word we do a BFS starting from beginWord

        We replace each char and see if it exists in wordList
        make wordList a set for easier lookup

        track iterations and we'll go
        Once a word is reached, we remove it from the set - to track visited words
        """
        import string

        wordList = set(wordList)
        alphabets = string.ascii_lowercase


        dq = deque([(1, beginWord)])

        while dq:
            curr_itr, curr_word = dq.popleft()

            if curr_word == endWord:
                return curr_itr

            for i in range(0, len(curr_word)):
                for alphabet in alphabets:
                    newWord = curr_word[:i] + alphabet + curr_word[i+1:]
                    if newWord in wordList:
                        wordList.remove(newWord)
                        dq.append((curr_itr+1, newWord))

        return 0