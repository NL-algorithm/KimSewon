# 11727
# 정사각형 1개로 2칸을 차지하는 경우
# 가로 직사각형 2개로 2칸을 차지하는 경우
# 세로 직사각형 1개로 1칸을 차지하는 경우
# 합이 n이 되는 2_a, 2_b, 1로 이루어진 수열의 개수
# 기존 결과에 부분중복 순열 (2_a, 2_b)를 배치하는 경우의 수를 곱한다.

# 피보나치
# dp[n] = dp[n-1] + 2 * dp[n-2]
# dp[0] = 0
# dp[1] = 1
# dp[2] = 3


N = int(input())
result = 0
# fact = [1] * (N+1)
# for i in range(1, N+1):
#     fact[i] = fact[i-1] * i

# for num2 in range((N // 2) + 1):
#     num1 = N - (num2*2)
#     for num2a in range(num2+1):
#         num2b = num2 - num2a
#         result += fact[num1+num2] // fact[num1] // fact[num2a] // fact[num2b]

dp = [0 for _ in range(max(3, N+1))]
dp[1] = 1
dp[2] = 3
for i in range(3, N+1):
    dp[i] = dp[i-1] + 2 * dp[i-2]
result = dp[N]

print(result % 10007)