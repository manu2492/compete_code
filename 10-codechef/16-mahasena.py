'''
Kattapa was known to be a very superstitious person. He believed that a soldier is 
"lucky" if the soldier is holding an even number of weapons, and "unlucky" otherwise. 
He considered the army as "READY FOR BATTLE" if the count of "lucky" soldiers is 
strictly greater than the count of "unlucky" soldiers, and "NOT READY" otherwise.

Input
The first line of input consists of a single integer N denoting the number of soldiers. 
The second line of input consists of N space separated integers A1, A2, ..., AN, 
where Ai denotes the number of weapons that the ith soldier is holding.

Output
Generate one line output saying "READY FOR BATTLE", if the army satisfies the 
conditions that Kattapa requires or "NOT READY" otherwise (quotes for clarity).


'''
n=int(input())
l=input().split()
even=0
odd=0
for i in l:
    if(int(i)%2==0):
        even+=1
    else:
        odd+=1
if(even>odd):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
