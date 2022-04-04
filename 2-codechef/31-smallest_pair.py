'''
You are given a sequence a1, a2, ..., aN. Find the smallest possible value of ai + aj, where 1 ≤ i < j ≤ N.

Input
The first line of the input contains an integer T denoting the number of test cases. The description of T 
test cases follows. 
The first line of each description consists of a single integer N.
The second line of each description contains N space separated integers - a1, a2, ..., aN respectively.

Output
For each test case, output a single line containing a single integer - the smallest possible sum for the 
corresponding test case.

Input:
1
4
5 1 3 4

Output:
4
'''
# o(n log n)

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort() 
    sum1 = arr[0] + arr[1]
    print(sum1)


# o(n)

