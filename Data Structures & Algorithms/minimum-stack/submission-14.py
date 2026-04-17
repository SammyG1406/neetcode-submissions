class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        self.current_min=float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<self.current_min:
            self.min_stack.append(val)
            self.current_min=val
        
        else:
            self.min_stack.append(self.current_min)
        print("\nstack", self.stack) 
        print("min_stack", self.min_stack)   

    def pop(self) -> None:
        print("\nPopping")
        self.current_min=self.min_stack[len(self.min_stack)-2]
        self.min_stack.pop()
        self.stack.pop()

        if len(self.min_stack)==0:
            self.current_min=float('inf')
        print("stack", self.stack) 
        print("min_stack", self.min_stack)  
        


        

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.min_stack[len(self.min_stack)-1]
        
