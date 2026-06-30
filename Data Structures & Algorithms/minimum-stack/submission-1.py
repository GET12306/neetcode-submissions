class MinStack:

    def __init__(self):
        self.stack = []
        self.mvalue = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.mvalue = val
        else:
            self.stack.append(val-self.mvalue)
            if val < self.mvalue:
                self.mvalue = val
        

    def pop(self) -> None:
        pop = self.stack.pop()

        if pop < 0:
            self.mvalue -= pop
        

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.mvalue
        else:
            return self.mvalue
        

    def getMin(self) -> int:
        return self.mvalue
        
