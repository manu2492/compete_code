'''
Chef in Vaccination Queue 
There are N people in the vaccination queue, Chef is standing on the Pth position from the front of the queue. 
It takes X minutes to vaccinate a child and Y minutes to vaccinate an elderly person. Assume Chef is an elderly 
person.

You are given a binary array A1,A2,…,AN of length N, where Ai=1 denotes there is an elderly person standing 
on the ith position of the queue, Ai=0 denotes there is a child standing on the ith position of the queue. 
You are also given the three integers P,X,Y. Find the number of minutes after which Chef's vaccination will 
be completed.

Sample Input 1 
3
4 2 3 2
0 1 0 1
3 1 2 3
1 0 1
3 3 2 2
1 1 1

Sample Output 1 
5
3
6
'''
t = int(input())

for i in range(t):
    n, p, x, y = map(int, input().split())

    a = list(map(int, input().split()))
    i = 0

    for j in range(0, p):
        if a[j] == 1:
            i += y
        else:
            i += x
    print(i)





































