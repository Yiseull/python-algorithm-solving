import sys
input = sys.stdin.readline


def solution(n, condos) -> int:
    answer = 0
    for i in range(n):
        x = True
        for j in range(n):
            if (condos[j][0] < condos[i][0] and condos[j][1] <= condos[i][1]) or ( condos[i][1] > condos[j][1] and condos[i][0] >= condos[j][0]):
                x = False
                break
        if x:
            answer += 1

    return answer


if __name__ == '__main__':
    n = int(input())
    condos = [tuple(map(int, input().split())) for _ in range(n)]
    print(solution(n, condos))