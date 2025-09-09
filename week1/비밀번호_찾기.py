import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
d = dict() # 딕셔너리 사용

for _ in range(N):
    url, password = input().rstrip().split()
    d[url] = password

for _ in range(M):
    st = input().rstrip()
    print(f"{d[st]}")