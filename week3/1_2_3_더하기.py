# 9095

dp = [0] * 11
dp[1] = 1
dp[2] = 2 # (1+1, 2)
dp[3] = 4 # (1+1+1, 2+1, 1+2, 3)
# dp[n] = dp[n-1] + dp[n-2] + dp[n-3] (1을 더하거나, 2를 더하거나, 3을 더하거나)

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(int(input())):
    n = int(input())
    print(f"{dp[n]}")

