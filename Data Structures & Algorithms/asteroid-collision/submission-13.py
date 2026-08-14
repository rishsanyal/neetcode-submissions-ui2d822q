
"""
+ve means right, -ve means left
abs value is it's size

smaller one explodes
if equal both explode

stack for this
"""



class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for asteroid in asteroids:
            if stack is None:
                stack.append(asteroid)
                continue

            add_asteroid = False

            while stack:
                previous_asteroid = stack[-1]

                prev_asteroid_side = True if previous_asteroid >= 0 else False
                curr_asteroid_side = True if asteroid >= 0 else False

                previous_asteroid_size = abs(previous_asteroid)
                curr_asteroid_size = abs(asteroid)

                if prev_asteroid_side == curr_asteroid_side:
                    # both +ve or both -ve
                    add_asteroid = True
                    break
                elif prev_asteroid_side and not curr_asteroid_side:
                    # prev asteroid +ve, curr -ve
                    if previous_asteroid_size > curr_asteroid_size:
                        add_asteroid = False
                        break
                    elif previous_asteroid_size < curr_asteroid_size:
                        add_asteroid = True
                        stack.pop()
                    else:
                        add_asteroid = False
                        stack.pop()
                        break
                else:
                    # prev -ve curr positive
                    add_asteroid = True
                    break

            if add_asteroid:
                stack.append(asteroid)

        return stack

