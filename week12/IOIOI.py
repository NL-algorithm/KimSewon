# 5525

# State Machine

N = int(input()) # IOIOIO...O (길이 2N+1) O가 N개
M = int(input())
S = input().rstrip() # 문자열

result = 0
count = 0
idx = 0

while idx < M - 2:
    if S[idx] == 'I' and S[idx+1] == 'O' and S[idx+2] == 'I':
        count += 1

        if count >= N:
            result += 1
        
        idx += 2

    else:
        count = 0
        idx += 1

print(result)

# Sliding Window (50점)
# N = int(input()) # IOIOIO...O (길이 2N+1) O가 N개
# checkString = 'IO' * N + 'I'
# length = 2 * N + 1
# M = int(input())
# S = input().rstrip() # 문자열

# result = 0

# for i in range(len(S) - length + 1):
#     if S[i:i + length] == checkString:
#         result += 1

# print(result)