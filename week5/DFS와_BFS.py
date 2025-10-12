# 1260

import sys
import bisect
input = sys.stdin.readline

N, M, V = map(int, input().rstrip().split())

tree = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().rstrip().split())
    bisect.insort_left(tree[u], v)
    bisect.insort_left(tree[v], u)
for i in range(1, N+1):
    tree[i] = sorted(tree[i])

def dfs(visited, tr, n):
    visited.append(n)
    for node in tr[n]:
        if node not in visited:
            dfs(visited, tr, node)

    return visited

def bfs(tr, n):
    visited = []
    queue = []
    visited.append(n)
    queue.append(n)

    while queue:
        node = queue.pop(0)
        for neighbor in tr[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    
    print(' '.join(map(str, visited)))
    return

print(' '.join(map(str, dfs([], tree, V))))
bfs(tree, V)
