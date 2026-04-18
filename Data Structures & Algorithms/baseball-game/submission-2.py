class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #operations array[with numbers and characters]
        #C means removing the entire score, D doubloes the score and stores it(D is not an operation)
        # C means removing the top result
        # last element isnt necessarily an operation, only operations seems to be +
        # if last element isnt an operation, just sum all of them
        # need to store the results continously, cant remove them unless C happens.
        # should store a stack that stores the sum of the results continosuly
        # repeat for each operations.
        # append to resstack if its a normal number and sumStack should add
        # if an + 

        resStack = [0]
        sumStack = [0]

        for char in operations:
            if char == "D":
                val = resStack[-1]
                val *= 2
                resStack.append(val)
                sumStack.append(sumStack[-1] + val)
            elif char == "C":
                sumStack.pop()
                resStack.pop()
            elif char == "+":
                val = resStack[-1] + resStack[-2]
                resStack.append(val)
                sumStack.append(sumStack[-1] + val)
            else:
                resStack.append(int(char))
                val = sumStack[-1] + int(char)
                sumStack.append(val)
            print(resStack, sumStack)
        
        return sumStack[-1]

        