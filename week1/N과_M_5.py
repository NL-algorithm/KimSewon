# 15654

# 순서 상관 없지만 중복 없음
import sys
import heapq as hq

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
visited = [False] * N # 중복 체크용

array = sorted(list(map(int, input().rstrip().split())))

def backtrack(arr):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return
    for i in range(N): # DFS
        if not visited[i]:
            visited[i] = True
            backtrack(arr + [array[i]])
            visited[i] = False

backtrack([])