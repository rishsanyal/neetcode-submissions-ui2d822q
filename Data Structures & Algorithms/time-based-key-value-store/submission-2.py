"""
We create a dict with the key as the given key
the value is a list where each element is (timestamp, value)

on set -> We just append the input value to the dict (assuming the insertions are in order)
on get -> We do a binary search to get the value, if it exists great else we return the leftmost index of where it should've existed
"""


class TimeMap:

    def __init__(self):
        self.tracker = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tracker[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        def __bs():
            l, r = 0, len(self.tracker[key])-1

            while l < r:
                mid = (l+r)//2
                mid_timestamp, mid_val = self.tracker[key][mid]

                if mid_timestamp == timestamp:
                    return mid
                elif mid_timestamp < timestamp:
                    l = mid + 1
                else:
                    r = mid

            return r

        idx = __bs()

        return self.tracker[key][idx][1]
        
