# 17351

# 가능한 모든 경로를 만들고 각 경로를 체크:
#   MOLA가 몇 번 나오는지 파싱, maximum 값을 반환
# DP: 좌표에 달하는 모든 경로 중 최대 MOLA 개수
# 상태 전이 (MOLA를 완성할 수 있는가?)
#   M을 만나면 1, MO: 2, MOL: 3, MOLA: 4 (완성되면 다음상태는 0으로 다시 시작)

import sys
sys.setrecursionlimit(2000) 
input = sys.stdin.readline

N = int(input())
pane = []
for _ in range(N):
    pane.append(input().rstrip())

dp = [[[-1] * 4 for _ in range(N)] for _ in range(N)]

dp[0][0][1 if pane[0][0] == 'M' else 0] = 0

for i in range(N):
    for j in range(N):
        curr_char = pane[i][j]

        for d_i, d_j in [(-1, 0), (0, -1)]:
            p_i, p_j = i + d_i, j + d_j

            if 0 <= p_i < N and 0 <= p_j < N:
                for p_k in range(4):
                    p_dp = dp[p_i][p_j][p_k]

                    # 길 없음
                    if p_dp == -1:
                        continue

                    if curr_char == 'M':
                        dp[i][j][1] = max(dp[i][j][1], p_dp)
                    elif curr_char == 'O' and p_k == 1:
                        dp[i][j][2] = max(dp[i][j][2], p_dp)
                    elif curr_char == 'L' and p_k == 2:
                        dp[i][j][3] = max(dp[i][j][3], p_dp)
                    elif curr_char == 'A' and p_k == 3: # 완성
                        dp[i][j][0] = max(dp[i][j][0], p_dp + 1)
                    else:
                        dp[i][j][0] = max(dp[i][j][0], p_dp)

print(max(dp[N-1][N-1]))