from typing import List
import random, collections

class Solution:
    def findJudge_slow(self, n: int, trust: List[List[int]]) -> int:
        most_voted, most_votes = -1, 0
        given, recieved = {}, {}

        for p1, p2 in trust:
            recieved[p2] = recieved.get(p2, 0) + 1
            given[p1] = given.get(p1, 0) + 1

            if recieved[p2] > most_votes:
                most_voted = p2
                most_votes = recieved[p2]
        
        if most_votes == n-1 and most_voted not in given:
            return most_voted

        return -1

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        
        given, recieved = {}, {}

        for p1, p2 in trust:
            recieved[p2] = recieved.get(p2, 0) + 1
            given[p1] = given.get(p1, 0) + 1

        for i in range(1, n+1):
            if i in recieved and recieved[i] == n-1 and i not in given:
                return i

        return -1

    def findJudge_fast(self, n: int, trust: List[List[int]]) -> int::
        score = [0] * (n+1)
        for (a, b) in trust:
            score[a] -= 1
            score[b] += 1
            
        for i in range(1, len(score)):
            if score[i] == n-1:
                return i
        return -1


def generate_test(sol):
    maxLength = 100
    people = random.randint(1, maxLength)
    votes_count = random.randint(0, maxLength*10)

    votes = []
    voted = {}

    winner = -1

    if bool(random.randint(0, 1)):
        winner = random.randint(1, people)

    for i in range(votes_count):
        p1 = random.randint(1, people)
        p2 = random.randint(1, people)

        if winner != -1 and ( p1 == winner or p2 == winner ):
            continue

        if p1 == p2: continue

        if p1 not in voted:
            voted[p1] = []

        if p2 not in voted[p1]:
            voted[p1].append(p2)
            votes.append([p1, p2])
            
    if winner != -1:
        winning_votes = [[i, winner] for i in range(1, people+1) if i != winner]
        votes.extend(winning_votes)
                

sol = Solution()
for i in range(200):
    generate_test(sol)
