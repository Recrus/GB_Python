def power(A, B):
    if B == 0:
        return 1
    elif B == 1:
        return A
    elif B % 2 == 0:
        temp = power(A, B // 2)
        return temp * temp
    else:
        temp = power(A, (B - 1) // 2)
        return temp * temp * A


A, B = map(int, input().split())
result = power(A, B)
print(result)
