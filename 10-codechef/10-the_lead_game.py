'''
Input
The first line of the input will contain a single integer N  indicating the number of rounds in the game. 
Lines 2,3,...,N+1 describe the scores of the two players in the N rounds. Line i+1 contains two integer 
Si and Ti, the scores of the Player 1 and 2 respectively

Output
Your output must consist of a single line containing two integers W and L, where W is 1 or 2 and 
indicates the winner and L is the maximum lead attained by the winner.

Example

Input:

5
140 82
89 134
90 110
112 106
88 90
Output:

1 58
'''

#solution
n = int(input())
l = 0
for i in range(n):
    s1, s2 = map(int, input().split())
    if s1 > s2:
        s = s1 - s2
        w = 2 
    elif s2 > s1:
        s = s2 - s1
        w = 1 

    if s > l:
        l = s
print(w, l)

#better solution
n = int(input())
player1_score = 0
Player2_score = 0
lead = 0
for i in range(n):
    score1, score2 = map(int, input().split())
    player1_score = player1_score + score1
    Player2_score = Player2_score + score2
    diff = player1_score - Player2_score

    if diff > 0 and diff > lead:
        lead = diff
        leader = 1
    elif diff < 0 and abs(diff) > lead:
        lead = abs(diff)
        leader = 2
print(leader,lead)



