'''
Ada's classroom contains N*M tables distributed in a grid with N rows and M columns. Each table is occupied 
by exactly one student.

Before starting the class, the teacher decided to shuffle the students a bit. After the shuffling, each table 
should be occupied by exactly one student again. In addition, each student should occupy a table that is 
adjacent to that student's original table, i.e. immediately to the left, right, top or bottom of that table.

Is it possible for the students to shuffle while satisfying all conditions of the teacher?

Input
The first line of the input contains a single integer T denoting the number of test cases. 
The description of T test cases follows.

The first and only line of each test case contains two space-separated integers N and M.

Sample Input 1 
2
3 3
4 4
Sample Output 1 
NO
YES
'''
t = int(input())

for i in range(t):
    o, p = map(int, input().split())
    
    if o % 2 != 0 and p % 2 != 0:
        print('NO')
    else:
        print('YES')
