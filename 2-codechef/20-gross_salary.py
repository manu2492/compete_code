t = int(input())
total = 0
k = 0
for i in range(t):
    n = int(input())
    if n >= 1500:
        k = (n * 0.98) + 500
        total = k + n
    else:
        total = n * 2

    print(total)

        
