"""
We have a dict where the key is the key and the value is a list
Timestamps are increasing, so we can just append it on every set

On get, we can do binary search for the left most value of that timestamp
(bisect_left) and return the value


"""




class TimeMap:

    def __init__(self):
        self.tracker = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tracker[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.tracker.get(key, [])

        def __bs():
            l, r = 0, len(values)-1

            while l <= r:
                mid = (l+r)//2
                mid_ts, mid_val = values[mid]

                if mid_ts <= timestamp:
                    # go right
                    l = mid + 1
                else:
                    # go left
                    r = mid - 1

            # check r
            if 0 <= r < len(values):
                return values[r][1]

            return ''

        return __bs()

                

        
