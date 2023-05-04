n = int(input())
set1 = set(map(int, input().split()))

m = int(input())
set2 = set(map(int, input().split()))

intersection = set1 & set2

for x in sorted(intersection):
    print(x)
