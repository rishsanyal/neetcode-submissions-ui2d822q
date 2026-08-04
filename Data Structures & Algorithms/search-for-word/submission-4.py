class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        neighbors = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        w = list(word)

        def check(x, y, word_list, visited):

            if word_list == []:
                return True

            if (not (0 <= x < len(board))) or (not (0 <= y < len(board[0]))):
                return False

            if board[x][y] != word_list[0]:
                return False

            visited.add((x, y))

            for (dx, dy) in neighbors:
                if ((x+dx), (y+dy)) in visited:
                    continue

                if status := check(x+dx, y+dy, word_list[1:], visited):
                    return True

            visited.remove((x, y))

            return False


        for x in range(len(board)):
            for y in range(len(board[0])):
                if check(x, y, w, set()):
                    return True


        return False