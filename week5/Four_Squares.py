# 17626

# 최소 개수의 제곱수 합
# 최대 수가 50000이므로 사용가능한 제곱수는 1부터 223까지

# N을 받아서 최대 제곱수 범위 내

import math

N = int(input().rstrip())
n = math.floor(N ** 0.5)

# def func(N, n):
#     if N == (n ** 2):
#         return 1

#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if N == (i ** 2) + (j ** 2):
#                 return 2
                
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             for k in range(1, n+1):
#                 if N == (i ** 2) + (j ** 2) + (k ** 2):
#                     return 3
    
#     # 모든 자연수는 넷 또는 그 이하의 제곱수의 합으로 표현될 수 있다.
#     return 4
# print(func(N, n))


# dp[N] = min(dp[N - n^2]) + 1
def func(N):
    dp = [5] * (N+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, N+1):
        minN = 5
        j = 1
        while j ** 2 <= i:
            minN = min(minN, dp[i - (j ** 2)] + 1)
            j += 1
        dp[i] = minN

    return dp[N]
print(func(N))


