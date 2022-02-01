'''
Three numbers A, B and C are the inputs. Write a program to find second largest among them.

-Input
The first line contains an integer T, the total number of testcases. Then T lines follow, 
each line contains three integers A, B and C.

Output
For each test case, display the second largest among A, B and C, in a new line

Example
Input
3 
120 11 400
10213 312 10
10 3 450

Output

120
312
10
'''
# t is the number of times
t = int(input())
for i in range(t):
    #the map function always return a list:
    #int() make strins to integers
    #input() ask for a number, in this case three times
    #split() return a list ej : '12 11 10' to ['12', '11', '10']
    a, b, c = map(int, input().split())
    #then we compare te numbers with a, b and c
    if a >= c and a>= b:
        if c > b:
            print(c)
        else:
            print(b)
    elif b >= c and b >=a:
        if c > a:
            print(c)
        else:
            print(a)
    else:
        if b > a:
            print(b)
        else:
            print(a)


