class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        for i in range(len(tokens)):
            try:
                self.stack.append(int(tokens[i]))
            except:
                n2 = self.stack.pop()
                n1 = self.stack.pop()
                self.stack.append(self.cal(n1, n2, tokens[i]))
        return self.stack[0]


    def cal(self, n1: int, n2: int, how: str) -> int:
        if how == "+":
            return n1 + n2
        if how == "-":
            return n1 - n2
        if how == "*":
            return n1 * n2
        return int(n1 / n2)