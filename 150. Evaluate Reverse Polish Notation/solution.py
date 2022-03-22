from typing import List
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c not in '+-*/':
                stack.append(int(c))
            else:
                r = stack.pop()
                l = stack.pop()

                if c == '+':
                    stack.append(l + r)
                elif c == '-':
                    stack.append(l - r)
                elif c == '*':
                    stack.append(l * r)
                else:
                    stack.append(int(float(l) / r))

        return stack[-1]
