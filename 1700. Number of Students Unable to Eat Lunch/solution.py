from typing import List
from collections import deque, Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sp, nos = 0, 0

        while students and nos < len(students):
            cs = students.popleft()

            if cs == sandwiches[sp]:
                sp += 1
                nos = 0
            else:
                students.append(cs)
                nos += 1

        return nos

    def countStudents_2(self, A: List[int], B: List[int]) -> int:
        count = Counter(A)
        n, k = len(A), 0
        while k < n and count[B[k]]:            
            count[B[k]] -= 1
            k += 1            
            
        return n - k

sol = Solution()
print(sol.countStudents_2([1,1,1,0,0,1], [1,0,0,0,1,1]))
