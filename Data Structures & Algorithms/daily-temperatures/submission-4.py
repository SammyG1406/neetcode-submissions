class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [[temperatures[-1], len(temperatures)-1]]
        res = [0] * len(temperatures)
        # the stack of maximums should be store up to that point in order
        for i in range(len(temperatures) - 2, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1][1] - i
            stack.append([temperatures[i], i])
        return res