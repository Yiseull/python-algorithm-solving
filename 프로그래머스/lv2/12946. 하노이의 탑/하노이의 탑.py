answer = []


def hanoi(n, start, via, end) -> None:
    if n == 1:
        answer.append([start, end])
        return
    
    hanoi(n - 1, start, end, via)
    answer.append([start, end])
    hanoi(n - 1, via, start, end)
    

def solution(n) -> list:
    hanoi(n, 1, 2, 3)
    return answer