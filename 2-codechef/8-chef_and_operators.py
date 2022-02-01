'''
Relational Operators are operators which check relatioship between two values. Given two numerical values A and B 
you need to help chef in finding the relationship between them that is,
First one is greater than second or,
First one is less than second or,
First and second one are equal.

Input
First line contains an integer T, which denotes the number of testcases. Each of the T lines contain two integers A and B.

Output
For each line of input produce one line of output. This line contains any one of the relational operators
'<' , '>' , '='.

Input:
3
10 20
20 10
10 10

Output:
<
>
=
'''
t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if a < b:
        print('<')

    elif a > b:
        print('>')

    else:
        print('=')


