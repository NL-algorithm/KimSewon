# 2606

nodeN = int(input())
edge = [set() for _ in range(nodeN + 1)] # 그냥 set() * N 하면 같은 set()를 참조함...
visited = [False] * (nodeN + 1)  

for _ in range(int(input())):
    a, b = map(int, input().split())
    edge[a].add(b)
    edge[b].add(a)

def dfs(node):
    for i in edge[node]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

dfs(1)
visited[1] = False

result = 0
for i in visited:
    if i == True:
        result += 1

print(result)
