# 11279

import sys
import heapq as hq

input = sys.stdin.readline

N = int(input().rstrip())
nums = []

# for _ in range(N):
#     w = int(input().rstrip())
#     if w != 0:
#         hq.heappush(nums, -w)
#     else:
#         if nums:
#             print(-hq.heappop(nums))
#         else:
#             print(0)

# 직접 구현

for _ in range(N):
    w = int(input().rstrip())
    if w != 0:
        nums.append(w)
        idx = len(nums) - 1
        while idx > 0:
            parent = (idx - 1) // 2
            if nums[parent] < nums[idx]:
                nums[parent], nums[idx] = nums[idx], nums[parent]
                idx = parent
            else:
                break
    else:
        if nums:
            print(nums[0])
            nums[0] = nums[-1]
            nums.pop()
            idx = 0
            while True:
                left = idx * 2 + 1
                right = idx * 2 + 2
                largest = idx
                if left < len(nums) and nums[left] > nums[largest]:
                    largest = left
                if right < len(nums) and nums[right] > nums[largest]:
                    largest = right
                if largest != idx:
                    nums[idx], nums[largest] = nums[largest], nums[idx]
                    idx = largest
                else:
                    break
        else:
            print(0)