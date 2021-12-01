import random

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ai, bi = len(a)-1, len(b)-1
        out = []

        c, s = 0, 0
        while ai >= 0 or bi >= 0:            
            ac = 0 if ai < 0 or a[ai] == '0' else 1
            bc = 0 if bi < 0 or b[bi] == '0' else 1

            s = ac + bc + c
            out.append(str(s % 2))
            c = 1 if s > 1 else 0

            ai -= 1
            bi -= 1

        if c: out.append('1')

        out.reverse()

        return ''.join(out)
