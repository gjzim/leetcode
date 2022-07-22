from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def visit(room):
            if visited[room]: return
            
            visited[room] = True
            for nextRoom in rooms[room]:
                visit(nextRoom)            
          
        visited = [False] * len(rooms)        
        visit(0)
            
        return all(visited)
        
