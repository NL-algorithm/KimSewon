# 11286

# 0을 받으면 출력 및 제거
# 0이 아니라면 추가

import sys
import heapq as hq
input = sys.stdin.readline

a = []

for _ in range(int(input())):
    x = int(input())
    
    if x == 0:
        if a:
            absv, v = hq.heappop(a)
            print(v)
        else:
            print(0)
    else:
        hq.heappush(a, (abs(x), x))