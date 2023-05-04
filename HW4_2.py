N = int(input())
arr = list()
for i in range(N):
    x = int(input())
    arr.append(x)

arr_count = list()
for i in range(N):
    sum_berries = arr[i] + arr[(i - 1) % N] + arr[(i + 1) % N]
    arr_count.append(sum_berries)

print(max(arr_count))
