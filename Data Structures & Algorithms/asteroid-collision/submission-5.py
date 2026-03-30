class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # use a stack
        # if positive (moving right), append to stack
        # if negative (moving left), try collisions while
        # still negative AND stack not empty
        # return final stack. if stack empty and
        # asteroids not empty yet, append negative asteroid to output
        # and continue iteration
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else: # asteroid < 0
                collided = False
                while stack and stack[-1] > 0:
                    prev = stack.pop()
                    if prev == -asteroid:
                        collided = True
                        break
                    elif prev > -asteroid:
                        stack.append(prev)
                        break
                    else: # -asteroid > prev
                        continue
                if (not stack or stack[-1] < 0) and not collided:
                    stack.append(asteroid)
        return stack

                    