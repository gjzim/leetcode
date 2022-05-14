import collections

class Solution:
    def numTilePossibilities_alt(self, tiles: str) -> int:
        def generate(cur, rest):
            if cur not in sequences:
                sequences.add(cur)
            
            for i in range(len(rest)):
                generate(cur + rest[i], rest[:i] + rest[i+1:])                
        
        sequences = set()
        generate('', tiles)
        
        return len(sequences) - 1

    def numTilePossibilities(self, tiles: str) -> int:
        self.factorials = (1, 1, 2, 6, 24, 120, 720, 5040)

        def generate(cur, pos, n):
            if pos < n:
                return  generate(cur, pos + 1, n) + \
                        generate(cur + tiles[pos], pos + 1, n)
                    
            if cur in sequences:
                return 0

            sequences.add(cur)
            return self.countUniqueParams(cur)
            
        sequences = set()
        tiles = sorted(tiles)
        return generate('', 0, len(tiles)) - 1

    def countUniqueParams(self, s):
        count = self.factorials[len(s)]
        chars = collections.Counter(s)
        
        for c in chars:
            count //= self.factorials[chars[c]]
            
        return count

