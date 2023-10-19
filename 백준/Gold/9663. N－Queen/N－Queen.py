import sys
input = sys.stdin.readline

n = int(input())
result = 0
board = [0] * n


def n_queen(row):
    if row == n:
        global result
        result += 1
        return

    for col in range(n):
        board[row] = col
        possible = True
        for i in range(row):
            if board[row] == board[i] or row - i == abs(board[row] - board[i]):
                possible = False
                break
        if possible:
            n_queen(row + 1)


n_queen(0)
print(result)