# 14940

# 목표지점에서 부터 BFS를 수행, 각 지점의 거리 저장

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]

start = None
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            start = (i, j)
            break
    if start:
        break

# BFS 수행
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    queue = deque()
    queue.append((sx, sy))
    dist[sx][sy] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if dist[nx][ny] == -1 and graph[nx][ny] == 1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

bfs(start[0], start[1])

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()

