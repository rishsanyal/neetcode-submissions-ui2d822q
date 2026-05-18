class LRUCache:

    def __init__(self, capacity: int):
        self.tracker = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.tracker:
            return -1

        val = self.tracker.get(key)
        self.tracker[key] = val
        self.tracker.move_to_end(key)

        return val


    def put(self, key: int, value: int) -> None:
        if key not in self.tracker and len(self.tracker) == self.cap:
            # Check if this pops the most recently inserted item
            self.tracker.popitem(last=False)

        self.tracker[key] = value
        self.tracker.move_to_end(key)

        


        
        
