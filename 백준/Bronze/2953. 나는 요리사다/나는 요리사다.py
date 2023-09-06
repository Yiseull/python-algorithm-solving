import sys
input = sys.stdin.readline

answer = [0, 0]
for i in range(5):
    scores = sum(map(int, input().split()))
    if answer[1] < scores:
        answer = [i + 1, scores]

print(answer[0], answer[1])