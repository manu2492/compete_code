t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    total = 0
    if a > 1000:
        total = (a * b) * 0.9
    else:
        total = (a * b)

    print(total)


