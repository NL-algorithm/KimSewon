# 2178

# bfs

from collections import deque
N, M = map(int, input().split())

ma = []
for _ in range(N):
    ma.append(list(input()))


def bfs():
    q = deque()
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    q.append((0, 0))
    while q:
        r, c = q.popleft()
        
        for t in [(1,0), (0,1), (-1, 0), (0, -1)]:
            dr = r + t[0]
            dc = c + t[1]
            if dc >= M or dc < 0 or dr >= N or dr < 0:
                continue
            
            if ma[dr][dc] == '0':
                continue

            if visited[dr][dc] != 0:
                continue
            
            visited[dr][dc] = visited[r][c] + 1

            q.append((dr, dc))

    print(visited[N-1][M-1])

bfs()