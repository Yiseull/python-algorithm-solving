from collections import deque


def solution(n,a,b):
    q = deque([i for i in range(1, n + 1)])
    round = 1
    
    while 1:
        n //= 2
        for i in range(n):
            player1 = q.popleft()
            player2 = q.popleft()

            if a in [player1, player2]:
                if b in [player1, player2]:
                    return round
                else:
                    q.append(a)
            elif b in [player1, player2]:
                q.append(b)
            else:
                q.append(player1)
        
        round += 1

    return round