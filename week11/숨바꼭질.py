# 1697

# bfs

from collections import deque as dq
N, K = map(int, input().split())

def bfs():
    q = dq([N])
    max_n = 100000
    visited = [0] * (max_n + 1)

    while q:
        x = q.popleft()
        t = visited[x]

        if x == K:
            return t

        for nx in (x + 1, x - 1, x * 2):
            if 0 <= nx <= max_n and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)

print(bfs())