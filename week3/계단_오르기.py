# 2579
# dp[N]: 2가지 케이스 필요 (연속 또는 비연속의 경우) 크로스해서 각각 할당해서 올라감

N = int(input())
stair = [0] + [int(input()) for _ in range(N)]
dp = [[0, 0] for _ in range(N+1)]

dp[1][0] = stair[1]
dp[1][1] = stair[1]
if N >= 2:
    dp[2][0] = stair[2]
    dp[2][1] = stair[1] + stair[2]

for i in range(3, N+1):
    dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + stair[i]
    dp[i][1] = dp[i-1][0] + stair[i]

print(max(dp[N][0], dp[N][1]))
