def is2X2(i, j, board):
    if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
        return True
    return False


def solution(m, n, board):
    answer = 0

    for i in range(m):
        board[i] = list(board[i])

    while 1:
        change = False
        block_2x2 = []
        # 2×2로 배치된 4개 블록 찾기
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] and is2X2(i, j, board):
                    block_2x2.append((i, j))

        # 찾은 블록 지우기
        for i, j in block_2x2:
            change = True
            if board[i][j]:
                board[i][j] = ''
                answer += 1
            if board[i + 1][j]:
                board[i + 1][j] = ''
                answer += 1
            if board[i][j + 1]:
                board[i][j + 1] = ''
                answer += 1
            if board[i + 1][j + 1]:
                board[i + 1][j + 1] = ''
                answer += 1

        # 빈 공간을 채우기
        for j in range(n):
            for i in range(m - 2, -1, -1):
                if board[i][j]:
                    tmp = 1
                    v = board[i][j]
                    pre = i
                    while i + tmp < m and board[i + tmp][j] == '':
                        pre = i + tmp
                        tmp += 1
                        
                    board[i][j] = ''
                    board[pre][j] = v

        # 지워진 블록이 없으면 종료
        if not change:
            break

    return answer