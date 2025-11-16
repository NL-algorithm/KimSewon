# 21736

import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = []
start = (0, 0)

for i in range(N):
    t = list(input().strip())
    for idx, c in enumerate(t):
        if c == 'I':
            start = (i, idx)
    graph.append(t)

count = 0
visited = [[False] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count

    visited[x][y] = True

    if graph[x][y] == 'P':
        count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and graph[nx][ny] != 'X':
                dfs(nx, ny)

dfs(start[0], start[1])
if count == 0:
    print("TT")
else:
    print(count)