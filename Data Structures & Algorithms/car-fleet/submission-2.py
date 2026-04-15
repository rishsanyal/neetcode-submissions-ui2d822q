class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        target = 12
        position = [10,8,0,5,3]
        speed = [2,4,1,1,3]

        12, 9, 7, 4, 2
        1, 3, 1, 4, 2

        -> 1,2,3

        target = 10
        position = [0, 4, 2]
        speed = [2, 1, 3]

        10,2 -> 5
        8,3 -> 2.3
        6,1 -> 6
        """

        fleets = 0

        info = [((target-i[0]), i[1]) for i in zip(position, speed)]
        info.sort()

        stack = []

        for distance, speed in info:
            if not stack or distance/speed > stack[-1]:
                stack.append(distance/speed)

        return len(stack)