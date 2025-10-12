# 9461

# 1 1 1 2 2 3 4 5 7 9 12 ... P(12) = 16 = P(11) + P(7)

# P(N) = P(N-1) + P(N-5) (N은 6부터 시작), N은 1부터 100까지
# N: 1, 2, 3, 4, 5 까지는 고정
# N: 0 일때 0

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6, 101):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(int(input().rstrip())):
    print(dp[int(input().rstrip())])