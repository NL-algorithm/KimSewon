# 1389

N, M = map(int, input().split())
edge = [set() for _ in range(N+1)]
result = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a].add(b)
    edge[b].add(a)

def bfs(start, end):
    if start == end:
        return 0
    
    queue = [(start, 0)]
    visited = [False] * (N + 1)
    visited[start] = True

    while queue:
        v, d = queue.pop(0)
        for i in edge[v]:
            if not visited[i]:
                if i == end:
                    return d + 1
                visited[i] = True
                queue.append((i, d+1))
    
    return float('inf')
        
for i in range(1, N+1):
    for j in range(1, N+1):
        result[i] += bfs(i, j)

min = float('inf')
for i in range(1, N+1):
    if result[i] < min:
        min = result[i]
        ans = i
print(ans)