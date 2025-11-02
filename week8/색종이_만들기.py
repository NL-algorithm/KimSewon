# 2630
# 분할 정복

blue = 0
white = 0

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

def check_color(x, y, size):
    global blue, white
    color = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                check_color(x, y, size // 2)
                check_color(x, y + size // 2, size // 2)
                check_color(x + size // 2, y, size // 2)
                check_color(x + size // 2, y + size // 2, size // 2)
                return
    if color == 1:
        blue += 1
    else:
        white += 1

check_color(0, 0, n)
print(white)
print(blue)