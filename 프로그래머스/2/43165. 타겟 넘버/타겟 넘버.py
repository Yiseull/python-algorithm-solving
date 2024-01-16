def dfs(numbers: list, target: int, index: int, result: int) -> None:
    if index == len(numbers):
        if result == target:
            global answer
            answer += 1
        return
    
    dfs(numbers, target, index + 1, result + numbers[index])
    dfs(numbers, target, index + 1, result - numbers[index])


def solution(numbers: list, target: int) -> int:
    global answer
    answer = 0
    dfs(numbers, target, 0, 0)
    return answer