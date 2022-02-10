'''
Input:
First line of input contains a single integer T, the number of test cases.
Each test is a single line containing a string S composed of only lowercase English alphabet.

Output:
For each test case, output on a separate line: "YES" if the string is a lapindrome and "NO" if it is not.

Input:
3
gaga
abcde
rotor

Output:
YES
NO
YES
'''

t=int(input())
for i in range(t):
    s=input()
    if len(s)%2==0:
        n=len(s)
        a=list(s[:n//2])
        b=list(s[n//2:])
        a.sort()
        b.sort()
        if a==b:
            print("YES")
        else:
            print("NO")
    else:
        n=len(s)
        a=list(s[:n//2])
        b=list(s[(n//2)+1:])
        a.sort()
        b.sort()
        if a==b:
            print("YES")
        else:
            print("NO")


