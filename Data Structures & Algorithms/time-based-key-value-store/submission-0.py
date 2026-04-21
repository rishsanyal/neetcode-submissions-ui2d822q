"""
- Set is straight forward but we need to store the values in an increasing order (let's assume they only insert in increasing order for now)
    - Especially since python dict's maintain order
    - There's no pop, so that works
- Then we need binary search to get the most recent entry by timestamp

Base DS: A dict
    key: 
        {
            "reserved_key": [time1, time2,...]
            time: value
        }

    set -> {alice: {1:happy}}
    get -> {alice, 1} -> happy
    get -> alice, 2 -> not in the dict, so binary search for most recent
"""

class TimeMap:

    def __init__(self):
        self.tracker = defaultdict(lambda: defaultdict(list))

    def __search(self, key_list, timestamp) -> int:
        "Returns the most recent timestamp, closest to timestamp."
        "Assuming key_list is in order."

        l, r = 0, len(key_list)-1
        res = min(key_list)

        while l <= r:
            mid = (l+r)//2

            if key_list[mid] > timestamp:
                r = mid - 1
            else:
                # key_list[mid] <= timestamp
                res = max(res, key_list[mid])
                l = mid + 1

        return res

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.tracker.get(key, {}):
            # We're updating an existing record.
            self.tracker[key]['reserved_timestamp'].append(timestamp)
        self.tracker[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        res = self.tracker.get(key, {}).get(timestamp, "")
 
        if (not self.tracker.get(key, {})):
            return res

        res = self.__search(self.tracker[key]['reserved_timestamp'], timestamp)

        print(res)
        
        return self.tracker.get(key, {}).get(res, '')
        
