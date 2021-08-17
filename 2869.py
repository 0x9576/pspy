import sys
A, B, V = map(int,sys.stdin.readline().split())
left, right = 0, V + 1
while left <= right:
    mid = (right + left) // 2
    if (A-B) * (mid-1) + A >= V:
        right -= 1
        answer = mid
    else:
        left += 1
print(mid)