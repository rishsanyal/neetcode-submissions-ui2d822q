"""

we know speed and distance, thus we know time too

[
    (3, 6, 2, 1),
    (3, 9, 3, 1)
]

- zip the lists
- Sort by (target - position) - distance
- we have time
- iterating through the list, if we see the top of the stack having more time, we become a fleet else we add to the stack

target = 10, position = [4,1,0,7], speed = [2,2,1,1]
[
    (4, 2),
    (1, 2),
    (0, 1),
    (7, 1)
]

[
    (3),
    (3),
    (4.5),
    (10)
]

[
    3,
    4.5,
    10
]

"""



class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: (x[0]))

        car_time = [(target-x[0])/x[1] for x in cars]

        while car_time:
            curr_car_time = car_time.pop()

            if not stack:
                stack.append(curr_car_time)
                continue

            if stack[-1] >= curr_car_time:
                continue
            else:
                stack.append(curr_car_time)

        return len(stack)



        