import sys

input = sys.stdin.readline

N = int(input())
l = sorted(list(map(int, input().rstrip().split())))

result = 0
for num, i in enumerate(l):
    result += (i * (N - num))

print(result)