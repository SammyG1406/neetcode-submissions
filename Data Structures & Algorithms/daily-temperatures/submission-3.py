class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # array of integers
        # temepratures[i] tells the temperature on the ith day
        # return an array result where result [i] is the number of days after the ith day a warmer temperature appear
        # if there is no day in the future where a warmer temperatyre
        # exists, it will be default 0
        # at a certain day, the only temperatures that can be considered
        # are the one on the days after
        # you'll want to store the maximum if you go from the end, bc if
        # you will want to compare woith the highest
        # if we know the index of the temperature where it will be higher,
        # res[i] = higher[i] - i
        # will need to store the index and the number itself
        # can use a stack

        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            stack.append((i, temperatures[i]))
            if len(stack) >= 2:
                res[i] = stack[-2][0] - i
        return res
        