# 1463
# ans[N] = min(ans[N-1], ans[N/3], ans[N/2]) + 1

import sys
print = sys.stdout.write

N = int(input().rstrip())
dp = [0] * (N + 1)
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(f"{dp[N]}")