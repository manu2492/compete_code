'''
Input
An input contains 2 integers A and B.

Output
Print a wrong answer of A-B. Your answer must be a positive integer containing the same number of digits 
as the correct answer, and exactly one digit must differ from the correct answer. 
Leading zeros are not allowed. If there are multiple answers satisfying the above 
conditions, anyone will do.

Sample Input
5858 1234
Sample Output
1624
'''
a, b = map(int, input().split())

n = abs(a - b)
print(n - 10)

#better solution
a,b=map(int,input().split())
c=a-b
if (c+1)%10==0:
    print(c-1)
else:
    print(c+1)







