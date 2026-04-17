class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']
        for char in tokens:
            if char not in operands:
                stack.append(int(char))
            if char == '+':
                val = stack.pop() + stack.pop()
                stack.append(val)
            if char == '*':
                val = stack.pop() * stack.pop()
                stack.append(val)
            if char == '/':
                a,b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            if char == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
        return stack[-1]