class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        stack.append([temperatures[-1], len(temperatures)-1])
        for i in range(len(temperatures)-2, -1, -1):
            counter = -1
            while stack and stack[-1][0] <= temperatures[i]:
                counter += 1
                stack.pop()
            stack.append([temperatures[i],i])
            if len(stack) >= 2:
                res[i] = stack[-2][1] - stack[-1][1]
            else:
                res[i] = 0
        return res
            