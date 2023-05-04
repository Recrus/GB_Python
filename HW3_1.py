N = int(input())
A = list(map(int, input().split()))
X = int(input())

count = 0

for i in range(N):
    if A[i] == X:
        count += 1

print(count)
