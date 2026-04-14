class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        use a stack here because we ONLY care about the asteroid on top
        for every incoming asteroid, we compare it against the previous one

        we pop if it explodes (bigger or eq asteroid comes in, in the other direction)
        we insert if it goes in the same direction

        asteroid_direction, asteroid
        """

        stack = []

        for asteroid in asteroids:
            asteroid_direction = "left" if asteroid < 0 else "right"
            
            if not stack or asteroid_direction == "right":
                stack.append((asteroid_direction, abs(asteroid)))
            else:
                if asteroid_direction == "left" and stack[-1][0] == "right":
                    # we compare
                    if abs(asteroid) >= stack[-1][1]:
                        stack.pop()
                elif asteroid_direction == "left" and stack[-1][0] == "left":
                    stack.append((asteroid_direction, abs(asteroid)))

        return [i[1] if (i[0] == "right") else -1*i[1] for i in stack]