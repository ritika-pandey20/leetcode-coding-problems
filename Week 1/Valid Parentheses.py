class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}':'{', ']': '['}
        for i in s:
            if i in mapping:
                if stack:
                    top = stack.pop()
                else:
                    top = '*'
                if mapping[i] !=top:
                    return False
            else: 
                stack.append(i)
        return not stack

                
        