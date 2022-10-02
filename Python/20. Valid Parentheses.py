class Solution:
    def isValid(self, s: str) -> bool:
        hp = {'(':')','{':'}','[':']'}
        stack = []
        for i in s:
            if(i in hp):
                stack.append(i)
            elif(len(stack) != 0 and hp[stack[-1]] == i):
                stack.pop()
            else:
                return False
        return len(stack) == 0
