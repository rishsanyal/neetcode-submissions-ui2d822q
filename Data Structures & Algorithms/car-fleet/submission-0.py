class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        target = 10
        position = [1, 4]
        speed = [3, 2]

        dist = [9, 6]

        speed = (target - pos)/time

        6/2 = 3
        9/3 = 3

        target = 10, position = [4,1,0,7]
        distance = [6, 9, 10, 3]
        speed = [2,2,1,1]

        [3, 6, 9, 10]
        [1, 2, 2, 1]
        [3, 3, 4.5, 10]

        - sort by position
        - use as a stack from the top
            - use 1 while loop and update fleet
        """

        fleets = 0

        info = [i for i in zip(position, speed)]
        info.sort()

        while info:
            curr = (target-info[-1][0])/info[-1][1]
            info.pop()
            while info and (curr == (target-info[-1][0])/info[-1][1]):
                info.pop()
            fleets += 1

        return fleets