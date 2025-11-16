# 30804

# left right two pointer

import sys
from collections import defaultdict

N = int(input())
t = list(input().split())

l = 0
cnt = defaultdict(int)
ans = 0
distinct = 0

for r, f in enumerate(t):
    if cnt[f] == 0:
        distinct += 1
    cnt[f] += 1

    while distinct > 2:
        l_f = t[l]
        cnt[t[l]] -= 1
        if cnt[t[l]] == 0:
            distinct -= 1
        l += 1

    ans = max(ans, r - l + 1)

print(ans)