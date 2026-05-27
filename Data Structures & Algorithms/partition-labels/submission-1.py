"""
We need to track the first and last index of every character
it's like intervals almost, we merge them and create a result?


"xyxxyzbzbbisl"

tracker: {
    x: (0, 3),
    y: (1, 4),
    z: (5, 7),
    b: (6, 9),
    i: (10, 10),
    s: (11, 11),
    l: (12, 12),
}

curr_min = last_index

we pop from dict
have curr_min
when curr_min changes or the next element doesn't meet it, we append to result

we use orderedDict


"abcabc"
tracker: {
    a: (0, 3),
    b: (1, 4),
    c: (2, 5),
}


"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        tracker = OrderedDict()
        
        for idx, char in enumerate(s):
            if char not in tracker:
                tracker[char] = [idx, idx]
            else:
                tracker[char][1] = idx
                tracker.move_to_end(char)

        curr_min = len(s) - 1
        curr_max = len(s) - 1
        res = []
        count = 0

        print(tracker)

        while tracker:
            _, (first_idx, last_idx) = tracker.popitem(last=True)

            # print(curr_min, curr_max)

            if (first_idx <= curr_min <= last_idx) or (first_idx <= curr_max <= last_idx) or (curr_min <= first_idx <= curr_max) or (curr_min <= last_idx <= curr_max):
                curr_min = min(first_idx, curr_min)
                curr_max = max(last_idx, curr_max)
            else:
                res.insert(0, curr_max - curr_min + 1)
                curr_min, curr_max = first_idx, last_idx

        res.insert(0, curr_max - curr_min + 1)

        return res


        