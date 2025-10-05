# 9375

import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    s = set()
    l = dict()
    for _ in range(int(input().rstrip())):
        _, a = map(str, input().rstrip().split())
        if a not in s:
            s.add(a)
            l[a] = 1
        l[a] += 1
    
    result = 1
    for i in l.values():
        result *= i
    
    print(result - 1)
        
        
