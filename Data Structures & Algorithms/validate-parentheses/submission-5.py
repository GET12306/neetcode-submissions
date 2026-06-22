class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        push_str = '([{'
        if s[0] not in push_str:
            return False
        if s[-1] in push_str:
            return False
        stack = []
        for i in s:
            if i in push_str:
                stack.append(i)
            else:
                last_b = stack.pop()
                if not self.isClosed(last_b, i):
                    return False
        return True if not stack else False


    def isClosed(self, b1: str, b2: str) -> bool:
        if b1 == "(" and b2 == ")":
            return True
        if b1 == "[" and b2 == "]":
            return True
        if b1 == "{" and b2 == "}":
            return True
        return False