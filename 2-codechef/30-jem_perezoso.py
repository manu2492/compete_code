'''
Jem will not take a break until he finishes at least half of the remaining problems. Formally, if N is even 
then he will take he first break after finishing N / 2 problems. If N is odd then the break will be after 
he done (N + 1) / 2 problems. Each of his break will last for B minutes. Initially, he takes M minutes in 
solving a problem, after each break he will take twice more time in solving a problem, i.e. 2 * M minutes per 
problem after the first break.

Example
Input:
2
9 1 2

Output:
45
'''

t = int(input())
for i in range(t):
    n, b, m = map(int, input().split())
    time = 0
    k = 0
    print(n, b, m, time, k)

    while n > 0:
        if n == 1:
            time = time + (n * m)
            n = n - 1
        elif n % 2 != 0:
            n += 1
            n = n / 2
            time = time + (n * m) + b
            m = m * 2
            n -= 1
        else:
            n = n / 2
            time = time + (n * m) + b
            m = m * 2

    print(time)

