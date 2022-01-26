'''
Small Factorial: 
Write a program to find the factorial value of any number entered by the user.
Input
The first line contains an integer T, the total number of testcases. Then T lines follow, 
each line contains an integer N.
Output
For each test case, display the factorial of the given number N in a new line

Example
Input
3 
3 
4
5

Output

6
24
120
'''

#my solution
t = int(input())

for i in range(t):
    n = int(input())
    for i in range(2, n):
        n *= i
    print(n)


#better solution(codechef)
n=int(input())
for i in range(n):
    m=1
    s=int(input())
    for j in range(s):
        m=m*(j+1)
    print(m)
















