#t = input()
#t = list(t)
#
#t.sort()
#
#def iterar():
#    
#
#    for i in t:
#        print(i)
#
#iterar()




#second solution
lis=[]
t=int(input())
while t>0:
    n=int(input())
    lis.append(n)
    t-=1
lis.sort()
for i in range(0,len(lis)):
    print(lis[i])



