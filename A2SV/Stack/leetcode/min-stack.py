class MinStack:

    def __init__(self):
        self.stack = []

        self.mymin =[]
        self.length = 0
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mymin:
            self.mymin.append(val)
        else:
            self.mymin.append( min(self.mymin[-1] , val))
        self.length+=1
        
        

    def pop(self) -> None:
        if self.length>0:
            self.stack.pop()
            self.mymin.pop()

        

    def top(self) -> int:
        return self.stack[-1]

        

    def getMin(self) -> int:
        return self.mymin[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()