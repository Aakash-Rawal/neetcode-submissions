class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for c in operations:
            if c == "D":
                total += stack[-1]*2
                stack.append(stack[-1]*2)
            elif c == "C":
                ele = stack.pop()
                total -= ele
            elif c == "+":
                total += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(c))
                total += int(c)
    
        return total

        