t = int(input())

#split

for i in range(t):
    a, b = map(int, input().split())

    if a > b:
        print(a, (a+b))
    else:
        print(b, (a+b))


