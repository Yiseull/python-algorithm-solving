import sys
input = sys.stdin.readline


m = int(input())
cup = [0, 1, 0, 0]
for _ in range(m):
    x, y = map(int, input().split())
    cup[x], cup[y] = cup[y], cup[x]

for i in range(1, 4):
    if cup[i]:
        print(i)
        exit(0)

print(-1)
