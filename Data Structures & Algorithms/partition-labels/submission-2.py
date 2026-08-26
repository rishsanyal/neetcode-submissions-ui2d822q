class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_tracker = defaultdict(lambda: [float('inf'), float('-inf')])
        res = []

        for (idx, char) in enumerate(s):
            char_tracker[char] = [
                min(char_tracker[char][0], idx),
                max(char_tracker[char][1], idx)
            ]

        values = list(char_tracker.values())
        values.sort(key=lambda x: x[0])

        curr_min, curr_max = values[0][0], values[0][1]
        curr_len = curr_max - curr_min

        print(values)

        for i in range(1, len(values)):
            new_min, new_max = values[i][0], values[i][1]

            if curr_min < new_min < curr_max:
                curr_max = new_max
            else:
                res.append(curr_max - curr_min + 1)

                curr_min = new_min
                curr_max = new_max

        return res + [(curr_max - curr_min + 1)]

        


        