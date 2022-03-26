'''
Devu and friendship testing

Devu has n weird friends. Its his birthday today, so they thought that this is the best occasion 
for testing their friendship with him. They put up conditions before Devu that they will break the 
friendship unless he gives them a grand party on their chosen day. Formally, ith friend will break his 
friendship if he does not receive a grand party on dith day.

Devu despite being as rich as Gatsby, is quite frugal and can give at most one grand party daily. Also, 
he wants to invite only one person in a party. So he just wonders what is the maximum number of friendships 
he can save. Please help Devu in this tough task !!

Sample Input 1 
2
2
3 2
2
1 1

Sample Output 1 
2
1
'''
t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    arr = []

    for j in a:
        if j not in arr:
            arr.append(j)
    k = int(len(arr))
    print(k)








