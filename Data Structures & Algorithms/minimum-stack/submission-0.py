class MinStack:

    def __init__(self):
        self.stack = list()
        self.stack.append(0)

    def push(self, val: int) -> None:
        if len(self.stack) == 1:
            self.stack[0] = int(1)
        
        self.stack.append(val)

        if self.stack[-1] < self.stack[self.stack[0]]:
            self.stack[0] = len(self.stack) - 1

    def pop(self) -> None:
        if len(self.stack) != 1:
            self.stack.pop()
        if len(self.stack) == 1:
            self.stack[0] = 0
        if self.stack[0] == len(self.stack):
            min_index = 1
            for i, val in enumerate(self.stack):
                min_val = self.stack[1]
                if i == 0:
                    continue
                if self.stack[i] < min_val:
                    min_index = i
            self.stack[0] = min_index

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.stack[0]]
