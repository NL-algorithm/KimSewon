# 5373

# 노가다

import sys
input = sys.stdin.readline

def rotate(p):
    t = [
        [p[2][0], p[1][0], p[0][0]],
        [p[2][1], p[1][1], p[0][1]],
        [p[2][2], p[1][2], p[0][2]]
    ]
    return t

# U D L F R B
# 0 1 2 3 4 5
def move(pane, cube):
    if pane == 'U':
        cube[0] = rotate(cube[0]) 
        t = cube[4][0][:]
        cube[4][0] = cube[5][0]
        cube[5][0] = cube[2][0]
        cube[2][0] = cube[3][0]
        cube[3][0] = t


    elif pane == 'D':
        cube[1] = rotate(cube[1])
        t = cube[2][2][:] # 리스트를 복사해야함 ([2][2]로 copy 하면 깊은 복사)
        cube[2][2] = cube[5][2]
        cube[5][2] = cube[4][2]
        cube[4][2] = cube[3][2]
        cube[3][2] = t

    elif pane == 'L':
        cube[2] = rotate(cube[2])
        t = [cube[1][0][0], cube[1][1][0], cube[1][2][0]]
        cube[1][0][0] = cube[3][0][0]; cube[1][1][0] = cube[3][1][0]; cube[1][2][0] = cube[3][2][0]
        cube[3][0][0] = cube[0][0][0]; cube[3][1][0] = cube[0][1][0]; cube[3][2][0] = cube[0][2][0]
        cube[0][0][0] = cube[5][2][2]; cube[0][1][0] = cube[5][1][2]; cube[0][2][0] = cube[5][0][2]
        cube[5][0][2] = t[2]; cube[5][1][2] = t[1]; cube[5][2][2] = t[0]

    elif pane == 'F':
        cube[3] = rotate(cube[3])
        t = cube[1][0][:]
        cube[1][0] = [cube[4][2][0], cube[4][1][0], cube[4][0][0]]
        cube[4][0][0] = cube[0][2][0]; cube[4][1][0] = cube[0][2][1]; cube[4][2][0] = cube[0][2][2]
        cube[0][2] = [cube[2][2][2], cube[2][1][2], cube[2][0][2]]
        cube[2][0][2] = t[0]; cube[2][1][2] = t[1]; cube[2][2][2] = t[2]
        
    elif pane == 'R':
        cube[4] = rotate(cube[4])
        t = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
        cube[1][0][2] = cube[5][2][0]; cube[1][1][2] = cube[5][1][0]; cube[1][2][2] = cube[5][0][0]
        cube[5][0][0] = cube[0][2][2]; cube[5][1][0] = cube[0][1][2]; cube[5][2][0] = cube[0][0][2]
        cube[0][0][2] = cube[3][0][2]; cube[0][1][2] = cube[3][1][2]; cube[0][2][2] = cube[3][2][2]
        cube[3][0][2] = t[0]; cube[3][1][2] = t[1]; cube[3][2][2] = t[2]

    elif pane == 'B':
        cube[5] = rotate(cube[5])
        t = cube[1][2][:]
        cube[1][2][0] = cube[2][0][0]; cube[1][2][1] = cube[2][1][0]; cube[1][2][2] = cube[2][2][0]
        cube[2][0][0] = cube[0][0][2]; cube[2][1][0] = cube[0][0][1]; cube[2][2][0] = cube[0][0][0]
        cube[0][0] = [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
        cube[4][0][2] = t[2]; cube[4][1][2] = t[1]; cube[4][2][2] = t[0]


def cubing(cmd, cube):
    pane, direction = cmd[0], cmd[1]

    if direction == '+':
        move(pane, cube)
    else:
        for _ in range(3):
            move(pane, cube)

for _ in range(int(input().rstrip())):
    _ = int(input().rstrip())

    # U D L F R B
    # 0 1 2 3 4 5
    cube = [
        [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
        [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
        [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
        [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
        [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']],
        [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
    ]

    commands = input().rstrip().split()
    for cmd in commands:
        cubing(cmd, cube)

    for row in cube[0]:
        print(''.join(row))
