# 15650

import sys

input = sys.stdin.readline

# 문제: 각 조합을 어떻게 일일히 구할 것인가? - 백트래킹

N, M = map(int, input().rstrip().split())
array = [i for i in range(1, N+1)]

def backtrack(last_idx, arr):
    if len(arr) == M: # 길이가 되면 종료
        print(" ".join(map(str, arr)))
        return
    for i in range(last_idx, N): # dfs
        backtrack(i+1, arr+[array[i]]) # 같은 거 선택 불가, 인덱스 증가
        
backtrack(0, [])