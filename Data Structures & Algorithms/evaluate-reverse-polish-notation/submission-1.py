import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numberStack=[]
        for item in tokens:
            try:
                num = int(item)
                numberStack.append(num)
            except ValueError:
                if item == "+":
                    val1 = numberStack.pop()
                    val2 = numberStack.pop()
                    numberStack.append(val1 + val2)
                if item == "-":
                    val1 = numberStack.pop()
                    val2 = numberStack.pop()
                    numberStack.append(val2 - val1) 
                if item == "*":
                    val1 = numberStack.pop()
                    val2 = numberStack.pop()
                    numberStack.append(val1 * val2)
                if item == "/":
                    val1 = numberStack.pop()
                    val2 = numberStack.pop()
                    numberStack.append(int(val2/val1))
        return numberStack[0]     
            
            
            
        