class Solution:
    def isValid(self, s: str) -> bool:
        open_p = '([{'
        stack = list()
        
        for p in s:
            if p in open_p:
                stack.append(p)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if abs(ord(p)-ord(prev)) > 2 :
                    return False
        
        return True if not stack else False