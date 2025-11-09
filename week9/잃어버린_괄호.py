# 1541

# 괄호를 적절히 쳐서 식의 값을 최소로 만든다.
# - 나오면 걍 오른쪽 숫자 다 빼버리면 되는거 아닌가

S = input() + 'e'

result = 0
numStr = []
flag = True # 더하기 먼저

for ch in S:
    if ch == '-':
        if flag == True:
            result += int(''.join(numStr))
        else:
            result -= int(''.join(numStr))
        flag = False
        # print(numStr)
        numStr.clear()
        continue
    elif ch == '+' or ch == 'e':
        if flag == True:
            result += int(''.join(numStr))
        else:
            result -= int(''.join(numStr))
        # print(numStr)
        numStr.clear()
        continue

    numStr.append(ch)

print(result)