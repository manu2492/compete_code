'''
You are given two sequences A1,A2,…,AN and B1,B2,…,BN. For each valid i, player i scored Ai goals and 
committed Bi fouls. For each goal, the player that scored it gets 20 points, and for each foul, 10 
points are deducted from the player that committed it. However, if the resulting number of points of some 
player is negative, this player will be considered to have 0 points instead.

You need to calculate the total number of points gained by each player and tell Alex the maximum of these values.

Sample Input 1 
2
3
40 30 50
2 4 20
1
0
10

Sample Output 1 
800
0
'''

t = int(input())
for i in range(t):
    n = int(input())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = []

    for i in range(n):
        score = (arr1[i] * 20) - (arr2[i] * 10)
        arr3.append(score)
    if max(arr3) <= 0:
        print('0')
    else:
        print(max(arr3))



