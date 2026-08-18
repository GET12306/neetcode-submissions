class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        ope = '+-*/'

        def cal(x, y, op):
            if op == '+':
                return x + y
            elif op == '-':
                return y - x
            elif op == '*':
                return x * y
            else:
                return int(y / x)

        for ele in tokens:
            if ele not in ope:
                stack.append(int(ele))
                # print(stack)
            else:
                a = stack.pop()
                b = stack.pop()
                c = cal(a, b, ele)
                stack.append(c)
                # print(stack)
        
        return stack[-1]