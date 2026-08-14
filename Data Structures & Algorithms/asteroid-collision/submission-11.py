
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

            # print(stack)

            previous_asteroid = stack[-1] if stack else None

            if previous_asteroid is None:
                stack.append(asteroid)
                continue

            add_asteroid = False

            while stack:
                prev_asteroid_side = True if previous_asteroid >= 0 else False
                curr_asteroid_side = True if asteroid >= 0 else False

                previous_asteroid_size = abs(previous_asteroid)
                curr_asteroid_size = abs(asteroid)

                if prev_asteroid_side == curr_asteroid_side:
                    # both +ve or both -ve
                    stack.append(asteroid)
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
                break

        return stack

