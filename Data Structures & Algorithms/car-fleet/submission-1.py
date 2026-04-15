class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        target = 12
        position = [10,8,0,5,3]
        speed = [2,4,1,1,3]

        12, 9, 7, 4, 2
        1, 3, 1, 4, 2

        -> 1,2,3
        """

        fleets = 0

        info = [i for i in zip(position, speed)]
        info.sort()

        while info:
            curr = (target-info[0][0])/info[0][1]
            info.pop(0)
            while info and (curr <= (target-info[0][0])/info[0][1]):
                info.pop(0)
            fleets += 1

        return fleets