class Solution:
    def isSubsequence_iter(self, s: str, t: str) -> bool:       
        sp, tp = 0, 0
        slen, tlen = len(s), len(t)
        
        while tp < tlen and sp < slen:
            if s[sp] == t[tp]:
                sp += 1

            tp += 1

        return sp == slen

    def isSubsequence_recur(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False

        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        else:
            return self.isSubsequence(s, t[1:])

    def isSubsequence(self, s: str, t: str) -> bool:
        s, t = '#'+s, '#'+t
        slen, tlen = len(s), len(t)
        
        table = [[False] * tlen for _ in range(slen)]
        for i, _ in enumerate(table[0]): table[0][i] = True

        for row in range(1, slen):
            for col in range(1, tlen):
                if s[row] == t[col]:
                    table[row][col] = table[row-1][col-1]
                else:
                    table[row][col] = table[row][col-1]

        return table[slen-1][tlen-1]
