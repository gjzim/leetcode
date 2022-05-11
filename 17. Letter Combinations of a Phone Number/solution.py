from typing import List

class Solution:
    def letterCombinations_alt(self, digits: str) -> List[str]:
        if digits == '': return []
        
        numToLetters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        if len(digits) > 1:
            output = []
            
            for comb in self.letterCombinations(digits[1:]):
                output += [letter + comb for letter in numToLetters[digits[0]]]
                                       
            return output            
        else:
            return list(numToLetters[digits[0]])

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '': return []
        
        def dfs(index, cur):
            if len(cur) == len(digits):
                res.append(cur)
            else:
                for l in numToLetters[digits[index]]:
                    dfs(index + 1, cur + l)

        numToLetters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []
        dfs(0, '')
        return res

