import sys
input = sys.stdin.readline


def solution(n, status, students) -> str:
    for student in students:
        if student[0] == 1:
            for i in range(student[1] - 1, n, student[1]):
                status[i] = 1 - status[i]
        else:
            index = student[1] - 1
            status[index] = 1 - status[index]
            max_range = min(n - student[1] + 1, student[1])
            for i in range(1, max_range):
                left = index + i
                right = index - i
                if status[left] == status[right]:
                    status[left] = 1 - status[left]
                    status[right] = 1 - status[right]
                else:
                    break

    return '\n'.join(' '.join(map(str, status[i:i+20])) for i in range(0, n, 20))


if __name__ == '__main__':
    n = int(input())
    status = list(map(int, input().split()))
    m = int(input())
    students = [tuple(map(int, input().split())) for _ in range(m)]
    print(solution(n, status, students))