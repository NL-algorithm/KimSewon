# 1074

import sys
input = sys.stdin.readline

N, r, c = map(int, input().rstrip().split())

prevnum = 0
for i in range(N):
    t = (2**(N-1-i))
    skipsize = t*t
    
    if r < t:
        rLow = True
    else:
        rLow = False
        r -= t


    if c < t:
        cLow = True
    else:
        cLow = False
        c -= t
    
    if rLow and not cLow:
        prevnum += skipsize
    elif not rLow and cLow:
        prevnum += (skipsize * 2)
    elif not rLow and not cLow:
        prevnum += (skipsize * 3)

print(prevnum)