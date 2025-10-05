# 11659
# 구간합: 각 구간까지의 합을 리스트로 새로 저장
# 필요한 구간은 Subtract로 빠르게 계산

import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().rstrip().split())

num = list(map(int, input().rstrip().split()))
numSum = [0]
for idx, n in enumerate(num):
    numSum.append(numSum[idx] + n)

for _ in range(M):
    i, j = map(int, input().rstrip().split())

    print(f"{numSum[j] - numSum[i-1]}\n")