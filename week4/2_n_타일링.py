# 11726
# 가로 직사각형 2개로 2칸을 차지하는 경우
# 세로 직사각형 1개로 1칸을 차지하는 경우
# 합이 n이 되는 2, 1로 이루어진 수열의 개수

# 부분 중복 순열
# 0, n: n! / n! = 1
# 1, n-2: n-1! / n-2! 1! = n-1
# 2, n-4:  = n-2! / n-4! 2! = n-2 n-3 / 2
# ...

# 피보나치를 따른다
# dp[n] = dp[n-1] + dp[n-2]
# dp[0] = 0
# dp[1] = 1

N = int(input())
result = 0


# fact = [1] * (N+1)
# for i in range(1, N+1):
#     fact[i] = fact[i-1] * i
# for num2 in range((N // 2) + 1):
#     num1 = N - (num2*2)
#     result += fact[num1+num2] // fact[num1] // fact[num2]

dp = [1 for _ in range(max(3,N+1))]
dp[1] = 1
dp[2] = 2
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

result = dp[N]
print(result % 10007)