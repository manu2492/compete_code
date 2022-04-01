'''
In the 2-D world of Flatland, the Circles were having their sports day and wanted to end it with a 
nice formation. So, they called upon Mr. Sphere from Spaceland for help. Mr Sphere decides to arrange the 
Circles in square formations. He starts with N Circles and forms the largest possible square using these 
Circles. He then takes the remaining Circles and repeats the procedure. A square of side S requires S2 Circles 
to create.

Find the number of squares he will be able to form at the end of the process.

Input:
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of a single integer N.

Output:
For each testcase, output a single integer denoting the number of squares.
'''
import math

t = int(input())

for i in range(t):
    n = int(input())
    count = 0

    while n > 0:
        #floor() method in Python returns the floor of x i.e., the largest integer not greater than x.
        s = math.floor(n**0.5)
        n -= s * s
        count += 1
    print(count)







        

