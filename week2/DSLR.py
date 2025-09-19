# 9019
import sys

from collections import deque as dq

input = sys.stdin.readline
print = sys.stdout.write

# tlqkf 어떻게 DSLR 최적화가 원인이었냐 ㅅㅂ 죽어라 메인로직만 수정했는데 ㅜㅜ
def D(n: int):
    return (2 * n) % 10000

def S(n: int):
    return 9999 if n == 0 else n - 1

def L(n: int):
    return ((n % 1000) * 10) + (n // 1000)

def R(n: int):
    return ((n % 10) * 1000) + (n // 10)

def bfs(start, end):
    visited = [False]*10000
    prev = [-1]*10000       # 이전 상태 저장
    ops = ['']*10000        # 이전 상태에서 어떤 명령어 썼는지 저장

    queue = dq([start])
    visited[start] = True

    while queue:
        cur = queue.popleft()
        if cur == end:
            break

        for op, func in [('D', D), ('S', S), ('L', L), ('R', R)]:
            nxt = func(cur)
            if not visited[nxt]:
                visited[nxt] = True
                prev[nxt] = cur
                ops[nxt] = op
                queue.append(nxt)

    # 경로 역추적
    result = []
    cur = end
    while cur != start:
        result.append(ops[cur])
        cur = prev[cur]
    return ''.join(result[::-1])
    
for _ in range(int(input())):
    start, end = map(int, input().split())
    print(f"{bfs(start, end)}\n")
