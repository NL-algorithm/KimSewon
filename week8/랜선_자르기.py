# 1654

# k개의 제각각의 랜선
# n개의 같은 길이 (최대)

import sys

input = sys.stdin.readline

k, n = map(int, input().rstrip().split())
nums = []
for _ in range(k):
    nums.append(int(input().rstrip()))

start = 1
end = max(nums)
result = 0

while start <= end:
    mid = (start + end) // 2
    
    count = 0
    for length in nums:
        count += length // mid
    
    if count >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

