a = 0
res = 0
while True:
    a = int(input("Write your number\n"))
    if 100 <= a <= 999:
        break

for digit in str(a):
    res += int(digit)

print(res)
