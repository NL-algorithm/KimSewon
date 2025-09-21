# 20057

import sys
import math
input = sys.stdin.readline

tLeft = [
    [-1,   -1,   0.02, -1,   -1],
    [-1,   0.1,  0.07, 0.01, -1],
    [0.05, 2,    0,    -1,   -1],
    [-1,   0.1,  0.07, 0.01, -1],
    [-1,   -1,   0.02, -1,   -1]
]

tRight = [
    [-1,   -1,   0.02, -1,   -1  ],
    [-1,   0.01, 0.07, 0.1,  -1  ],
    [-1,   -1,   0,    2,    0.05],
    [-1,   0.01, 0.07, 0.1,  -1  ],
    [-1,   -1,   0.02, -1,   -1  ]
]

tUp = [
    [-1,   -1,   0.05, -1,   -1  ],
    [-1,   0.1,  2,    0.1,  -1  ],
    [0.02, 0.07, 0,    0.07, 0.02],
    [-1,   0.01, -1,   0.01, -1  ],
    [-1,   -1,   -1,   -1,   -1  ]
]

tDown = [
    [-1,   -1,   -1,   -1,   -1  ],
    [-1,   0.01, -1,   0.01, -1  ],
    [0.02, 0.07, 0,    0.07, 0.02],
    [-1,   0.1,  2,    0.1,  -1  ],
    [-1,   -1,   0.05, -1,   -1  ]
]

out_sand = 0
N = int(input().rstrip())
grid = [[-1 for _ in range(N + 4)] for _ in range(N + 4)]
for i in range(N):
    row = list(map(int, input().rstrip().split()))
    for j in range(N):
        grid[i + 2][j + 2] = row[j]

# left: 0, down: 1, right: 2, up: 3
def move(vec, pos):
    global out_sand
    if vec == 0:  # left
        tornado = tLeft
        nextPos = (pos[0], pos[1] - 1)
    elif vec == 1:  # down
        tornado = tDown
        nextPos = (pos[0] + 1, pos[1])
    elif vec == 2:  # right
        tornado = tRight
        nextPos = (pos[0], pos[1] + 1)
    elif vec == 3:  # up
        tornado = tUp
        nextPos = (pos[0] - 1, pos[1])

    # 토네이도가 이동할 다음 위치의 모래를 뿌림
    sand = grid[nextPos[0]][nextPos[1]]
    if sand == 0:
        return nextPos
    grid[nextPos[0]][nextPos[1]] = 0
    
    total_scattered = 0
    for i in range(5):
        for j in range(5):
            if tornado[i][j] == -1:
                continue
            
            ni = nextPos[0] + i - 2
            nj = nextPos[1] + j - 2
            
            if tornado[i][j] == 0:
                continue
            elif tornado[i][j] == 2:
                # α 위치에는 나중에 남은 모래를 모두 보냄
                alpha_ni, alpha_nj = ni, nj
                continue
            else:
                temp = math.floor(sand * tornado[i][j])
                total_scattered += temp
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != -1:
                    grid[ni][nj] += temp
                else:
                    out_sand += temp
                    
    # 나머지 모래 alpha로
    remaining_sand = sand - total_scattered
    if 0 <= alpha_ni < len(grid) and 0 <= alpha_nj < len(grid[0]) and grid[alpha_ni][alpha_nj] != -1:
        grid[alpha_ni][alpha_nj] += remaining_sand
    else:
        out_sand += remaining_sand

    return nextPos

startNum = N//2 + 2
pos = (startNum, startNum)
vec = 0
moveamount = 1
while pos != (2, 2):
    # 왼쪽으로 moveamount만큼
    for _ in range(moveamount):
        pos = move(vec, pos)
        if pos == (2, 2):
            break
    if pos == (2, 2):
        break

    # 아래로 moveamount만큼
    vec = (vec + 1) % 4  # down
    for _ in range(moveamount):
        pos = move(vec, pos)
        if pos == (2, 2):
            break
    if pos == (2, 2):
        break

    moveamount += 1

    # 오른쪽으로 moveamount만큼
    vec = (vec + 1) % 4  # right
    for _ in range(moveamount):
        pos = move(vec, pos)
        if pos == (2, 2):
            break
    if pos == (2, 2):
        break

    # 위로 moveamount만큼
    vec = (vec + 1) % 4  # up
    for _ in range(moveamount):
        pos = move(vec, pos)
        if pos == (2, 2):
            break
    if pos == (2, 2):
        break

    moveamount += 1
    vec = (vec + 1) % 4  # left

print(out_sand)