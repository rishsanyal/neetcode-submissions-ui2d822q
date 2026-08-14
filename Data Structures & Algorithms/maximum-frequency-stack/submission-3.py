"""

stack ?

Freq counter for each number
list of numbers per freq

{
    5: 1,
    7: 1,
    4: 1
}

{   
    1: [7, 5]
}

5, 7, 5, 4

"""

class FreqStack:
    def __init__(self):
        self.freq_count = defaultdict(int)
        self.stacks = defaultdict(list)

        self.curr_max_freq = 0
        
    def push(self, val: int) -> None:
        curr_freq = self.freq_count.get(val, 0) + 1

        self.stacks[curr_freq].insert(0, val)
        self.freq_count[val] += 1

        self.curr_max_freq = max(self.curr_max_freq, curr_freq)

    def pop(self) -> int:
        popped_num = self.stacks[self.curr_max_freq].pop(0)

        self.freq_count[popped_num] -= 1

        if not self.stacks[self.curr_max_freq]:
            self.curr_max_freq -= 1

        return popped_num
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()