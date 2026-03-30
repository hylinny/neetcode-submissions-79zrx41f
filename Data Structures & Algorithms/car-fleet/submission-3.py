class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair positions and speed and sort them
        # for each position-speed pair, we check
        # if difference * delta speed (curr - prev) >= prev difference to target,
        # we can merge
        # then, we can keep prev position & speed on the stack
        # else, we append to stack
        # return len of stack
        array = []
        for i in range(len(position)):
            array.append((position[i], speed[i]))
        array.sort(reverse=True)

        stack = []
        stack.append((target - array[0][0]) / array[0][1])

        for i in range(1, len(array)):
            timeToReach = (target - array[i][0]) / array[i][1]
            if timeToReach <= stack[-1]:
                continue
            stack.append(timeToReach)     

        return len(stack)

        # array = [(8, 2), (6, 3)]

        # array = [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]

        # position = [7, 4, 1, 0]
        # speed = [1, 2, 2, 1]
        # stack = [(7, 1), (1, 2), (0, 1)]


        # array = [(4, 2), (1, 3)]
