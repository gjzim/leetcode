from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0] * n
        
        for start, end, increment in bookings:
            result[start - 1] += increment
            if end < n:
                result[end] -= increment
                
        for i in range(1, n):
            result[i] += result[i - 1]
            
        return result
