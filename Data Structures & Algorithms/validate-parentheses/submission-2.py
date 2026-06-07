class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        carTable ={')':'(',']':'[', '}':'{'}

        for car in s:
            if car not in carTable:
                stack.append(car)
                continue
            if not stack or carTable[car] != stack[-1]:
                return False
            stack.pop()
        return not stack