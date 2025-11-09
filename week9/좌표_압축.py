# 18870

_ = input()
X = list(map(int, input().split()))
s = sorted(set(X))
d = dict(zip(s, range(len(s))))
print(*[d[i] for i in X])
