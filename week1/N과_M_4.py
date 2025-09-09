# 15652

import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
array = [i for i in range(1, N+1)]

def backtrack(last_idx, arr):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return
    for i in range(last_idx, N): # dfs
        backtrack(i, arr+[array[i]]) # 인덱스 그대로 (중복 ok)

backtrack(0, [])