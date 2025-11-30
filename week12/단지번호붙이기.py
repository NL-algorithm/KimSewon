# 2667

# 1을 만나면 그자리에서 1이 있는 곳을 bfs, 개수를 저장
# visited로 방문 처리, 방문한 곳은 1이더라도 스킵처리
# string에 유의

import sys
from collections import deque as dq

input = sys.stdin.readline

N = int(input().rstrip())
M = list(input().rstrip() for _ in range(N))
visited = [[False for _ in range(N)] for _ in range(N)]

nums = []

for r in range(N):
    for c in range(N):
        if visited[r][c] == False and M[r][c] == '1':
            count = 1
            q = dq()
            q.append((r,c))
            visited[r][c] = True
            
            while q:
                tr, tc = q.popleft()
                
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = tr + dr, tc + dc
                    
                    if 0 <= nr < N and 0 <= nc < N:
                        if visited[nr][nc] == False and M[nr][nc] == '1':
                            count += 1
                            q.append((nr,nc))
                            visited[nr][nc] = True

            nums.append(count)

nums.sort()
print(len(nums))
for num in nums:
    print(num)