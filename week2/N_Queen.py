# 9663
# (x + n, y), (x, y + n), (x + n, y + n) 는 제외된다.


global result
result = 0
# def nqueen(n, c_row, cols):
#     global result
#     if c_row == n:
#         result += 1
#         return
    
#     for col in range(n):
#         flag = True
#         for r, c in enumerate(cols):
#             if c == col or abs(c_row - r) == abs(col - c):
#                 flag = False
#                 break
        
#         if flag:
#             nqueen(n, c_row+1, cols+[col])
        
# N = int(input())
# nqueen(N, 0, [])
# print(result)


# set를 이용한 최적화
def nqueen(n, row=0, cols=set(), pos_diag=set(), neg_diag=set()):
    global result

    if row == n:
        result += 1
        return
    for col in range(n):
        if (col in cols) or ((row + col) in pos_diag) or ((row - col) in neg_diag):
            continue
        cols.add(col)
        pos_diag.add(row + col)
        neg_diag.add(row - col)
        nqueen(n, row + 1, cols, pos_diag, neg_diag)
        cols.remove(col)
        pos_diag.remove(row + col)
        neg_diag.remove(row - col)

N = int(input())
nqueen(N, 0, set(), set(), set())
print(result)
