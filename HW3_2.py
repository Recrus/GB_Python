N = int(input())
A = list(map(int, input().split()))
X = int(input())

diff = float('inf')
closest = None

for i in range(N):
    cur_diff = abs(A[i] - X)
    if cur_diff < diff:
        diff = cur_diff
        closest = A[i]

print(closest)
