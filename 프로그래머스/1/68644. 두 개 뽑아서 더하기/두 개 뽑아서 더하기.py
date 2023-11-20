from itertools import combinations

def solution(numbers) -> list:
    answer = set()
    for com in combinations(numbers, 2):
        answer.add(sum(com))
        
    return sorted(answer)