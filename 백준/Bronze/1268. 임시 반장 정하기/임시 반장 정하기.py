import sys
input = sys.stdin.readline


def solution(n, students) -> int:
    answer = [0, 0]
    for i in range(n):
        friends = set()
        for j in range(n):
            if i == j:
                continue
            for w in range(5):
                if students[i][w] == students[j][w]:
                    friends.add(j)
        count = len(friends)
        if count > answer[0]:
            answer = [count, i]

    return answer[1] + 1


if __name__ == '__main__':
    n = int(input())
    students = [tuple(map(int, input().split())) for _ in range(n)]
    print(solution(n, students))