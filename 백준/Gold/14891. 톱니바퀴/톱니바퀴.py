import sys
input = sys.stdin.readline


def isSame(gear1, gear2, gears) -> bool:
    if gear1 < gear2:
        if gears[gear1][2] != gears[gear2][6]:
            return False
    else:
        if gears[gear1][6] != gears[gear2][2]:
            return False
    return True


def rotate_gear(gear, gears, direction) -> None:
    if direction == 1:
        gears[gear] = gears[gear][-1] + gears[gear][:-1]
    else:
        gears[gear] = gears[gear][1:] + gears[gear][0]


def calculate_scores(gears) -> int:
    scores = 0
    tmp = 1
    for gear in gears:
        if gear[0] == '1':
            scores += tmp
        tmp *= 2
    return scores


def solution(gears, k, rotation) -> int:
    for gear, direction in rotation:
        rotation_list = [(gear - 1, direction)]
        tmp = -1
        for i in range(gear - 1, 0, -1):
            if isSame(i, i - 1, gears):
                break
            rotation_list.append((i - 1, direction * tmp))
            tmp *= -1
        tmp = -1
        for i in range(gear - 1, 3):
            if isSame(i, i + 1, gears):
                break
            rotation_list.append((i + 1, direction * tmp))
            tmp *= -1
        for g, d in rotation_list:
            rotate_gear(g, gears, d)

    return calculate_scores(gears)


if __name__ == '__main__':
    gears = [input().rstrip() for _ in range(4)]
    k = int(input())
    rotation = [tuple(map(int, input().split())) for _ in range(k)]
    print(solution(gears, k, rotation))