class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        while mask < num:
            mask = (mask << 1) + 1            
        
        return num ^ mask

    def findComplement_simpler(self, num: int) -> int:
        mask = 1
        while mask <= num:
            mask = mask << 1
        return (mask - 1) ^ num

    
