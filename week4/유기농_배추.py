# 1012

# 각 트리를 생성
# 트리에 인접노드가 있는가를 확인
# 예외상항: 떨어져있는 두 트리를 다른 노드가 연결하는 경우
# 후발 노드를 기준으로 다시 짜는게 맞는거 같은데?
# 인접 노드가 포함된 모든 트리를 자기가 루트가 되어 재구성 -> 모든 트리검사

# 인접 리스트 활용

for _ in range(int(input())):
    X, Y, K = map(int, input().rstrip().split())

    tree = []
    for _ in range(K):
        x, y = map(int, input().rstrip().split())

        adjN = {(x-1, y), (x+1, y), (x, y-1), (x, y+1)}

        tempTree = []
        for t in tree[:]:
            if t & adjN: # 집합간 교집합도 된데요
                tempTree.append(t)
                tree.remove(t)
        
        new_tree = set()
        for t in tempTree:
            new_tree |= t # 합집합 연산
        new_tree.add((x,y))

        tree.append(new_tree)

    print(len(tree))
            
