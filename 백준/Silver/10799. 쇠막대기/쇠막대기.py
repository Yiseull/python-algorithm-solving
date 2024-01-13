import sys
input = sys.stdin.readline


def solution(bars: int) -> int:
    answer = 0
    stack = [] 

    for i, parentheses in enumerate(bars):
        if parentheses == '(':
            stack.append(0)
        elif bars[i - 1] == '(':
            stack.pop()
            for j in range(len(stack)):
                stack[j] += 1
        else:
            answer += stack.pop() + 1

    return answer


if __name__ == '__main__':
    bars = input().rstrip()
    print(solution(bars))