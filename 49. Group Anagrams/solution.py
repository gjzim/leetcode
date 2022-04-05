from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams_mine(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s))

            result[key].append(s)
        
        return result.values()

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return result.values()

sol = Solution()
print(sol.groupAnagrams_mine(["eat","tea","tan","ate","nat","bat"]))
