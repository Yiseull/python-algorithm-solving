import sys
input = sys.stdin.readline


def create_cloud(visited):
    new_cloud = []
    for x in range(n):
        for y in range(n):
            if a[x][y] > 1 and (x, y) not in visited:
                a[x][y] -= 2
                new_cloud.append([x, y])

    return new_cloud


def water_copy_bug():
    visited = set()
    for c in cloud:
        cnt = 0
        for dx, dy in [[-1, -1], [-1, 1], [1, 1], [1, -1]]:
            next_x = dx + c[0]
            next_y = dy + c[1]
            if 0 <= next_x < n and 0 <= next_y < n and a[next_x][next_y]:
                cnt += 1
        a[c[0]][c[1]] += cnt
        visited.add((c[0], c[1]))

    return visited


def move_and_increase() -> None:
    i, j = 0, 0
    if 5 < d < 9: i = 1 * s
    elif 1 < d < 5: i = -1 * s
    if 3 < d < 7: j = 1 * s
    elif 0 < d < 3 or d == 8: j = -1 * s

    for c in cloud:
        c[0] += i
        c[1] += j
        while c[0] < 0: c[0] += n
        while c[0] >= n: c[0] -= n
        while c[1] < 0: c[1] += n
        while c[1] >= n: c[1] -= n

        a[c[0]][c[1]] += 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    move = [list(map(int, input().split())) for _ in range(m)]
    cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

    for d, s in move:
        move_and_increase()
        cloud = create_cloud(water_copy_bug())

    print(sum(map(sum, a)))
