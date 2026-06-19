"""
- We need a counter dict to count the frequency
- We need a list with frequency as it's index

We use the list and add numbers to the index according to it's frequency
"""



class FreqStack:

    def __init__(self):
        self.tracker = defaultdict(int)
        self.stacks = []
        
    def push(self, val: int) -> None:
        self.tracker[val] += 1

        while len(self.stacks) <= self.tracker[val]:
            self.stacks.append([])

        self.stacks[self.tracker[val]].append(val)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        ans = self.stacks[-1].pop()
        self.tracker[ans] -= 1

        return ans
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()