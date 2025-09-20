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
    elif vec == 1:  # down
        tornado = tDown
    elif vec == 2:  # right
        tornado = tRight
    elif vec == 3:  # up
        tornado = tUp
    
    sand = grid[pos[0]][pos[1]]
    if sand == 0:
        return
    grid[pos[0]][pos[1]] = 0
    
    total_scattered = 0
    for i in range(5):
        for j in range(5):
            if tornado[i][j] == -1:
                continue
            
            ni = pos[0] + i - 2
            nj = pos[1] + j - 2
            
            if tornado[i][j] == 0:
                continue
            elif tornado[i][j] == 2:
                # α 위치에는 나중에 남은 모래를 모두 보냄
                alpha_ni, alpha_nj = ni, nj
                continue
            else:
                temp = math.floor(sand * tornado[i][j])
                total_scattered += temp
                if grid[ni][nj] != -1:
                    grid[ni][nj] += temp
                else:
                    out_sand += temp
                    
    # 나머지 모래 alpha로
    remaining_sand = sand - total_scattered
    if grid[alpha_ni][alpha_nj] != -1:
        grid[alpha_ni][alpha_nj] += remaining_sand
    else:
        out_sand += remaining_sand

