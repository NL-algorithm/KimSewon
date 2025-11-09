# 18111
# 반례 ㅈㄴ 많네에

import sys
input = sys.stdin.readline

N, M, B = map(int, input().rstrip().split())

blocks = []
for _ in range(N):
    t = list(map(int, input().rstrip().split()))
    B += sum(t)
    blocks.append(t)

# 초기 h 설정
end_h = min(256, B // (N * M))

def calcCost(h):
    # 경계값 처리
    if h > end_h or h < 0:
        return float("inf")
    cost = 0
    for i in range(N):
        for j in range(M):
            t = blocks[i][j] - h
            if t > 0: # 블럭을 빼야하는 경우 2초
                t *= 2
            else: # 블럭을 넣어야하는 경우 1초
                t = abs(t)
            cost += t
    return cost

# def findMinCost(h, curr_cost):
#     next_cost = calcCost(h-1)
#     if h == 0:
#         return curr_cost, h
#     elif next_cost < curr_cost:
#         h -= 1
#         return findMinCost(h, next_cost)
#     else:
#         return curr_cost, h
# print(' '.join(map(str, findMinCost(end_h, calcCost(end_h)))))

def findMinCost(h, max_h, curr_cost):
    next_cost = calcCost(h+1)   
    prev_cost = calcCost(h-1)
    if h == 0:
        if curr_cost < next_cost:
            return curr_cost, h
        else:
            return findMinCost(h+1, max_h, next_cost)
    elif h == max_h:
        if curr_cost <= prev_cost:
            return curr_cost, h
        else:
            return findMinCost(h-1, max_h, prev_cost)
    else:
        if curr_cost >= next_cost:
            return findMinCost(h+1, max_h, next_cost)
        elif curr_cost > prev_cost:
            return findMinCost(h-1, max_h, prev_cost)
        else:
            return curr_cost, h
print(' '.join(map(str, findMinCost(end_h // 2, end_h, calcCost(end_h // 2)))))
# 이 경우 경계에서 calcCost 지정 범위 밖의 cost가 매우 적은게 문제였음
# 반레: 71 71 0
# 1 1 1 1 1 ... 1
# 1     ...     1
#       ...
# 1  ...  1 1 1 0
# h = 1 일때 지정 범위를 무시하고 넘어가 계산, cost가 1이 되버림