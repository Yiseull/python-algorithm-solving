def solution(x, y, n) -> int:
    MAX = 1000000
    dp = [MAX] * (y + 1)
    dp[x] = 0
    
    for i in range(x + 1, y + 1):
        if dp[i - n] != MAX:
            dp[i] = dp[i - n] + 1
        if i % 2 == 0 and dp[i // 2] != MAX:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0 and dp[i // 3] != MAX:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return -1 if dp[y] == MAX else dp[y]