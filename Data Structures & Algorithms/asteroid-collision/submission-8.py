class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            asteroid_direction = "left" if asteroid < 0 else "right"
            if not stack:
                add = True
            else:
                curr_direction, curr_asteroid = stack[-1]
                add = False
                if curr_direction == asteroid_direction or (curr_direction == "left" and asteroid_direction == "right"):
                    add = True
                else: # if (curr_direction == "right" and direction == "left"):
                    while stack and (curr_direction == "right" and asteroid_direction == "left"):
                        if abs(asteroid) == curr_asteroid:
                            stack.pop()
                            add = False
                            break
                        elif abs(asteroid) > curr_asteroid:
                            stack.pop()
                            add = True
                        elif abs(asteroid) < curr_asteroid:
                            add = False
                            break

                        if stack:
                            curr_direction, curr_asteroid = stack[-1]

            if add:
                stack.append((asteroid_direction, asteroid))

        # print(stack)
        return [i[1] for i in stack]