# cook your dish here
t = int(input())
coordinate = 0
for i in range(t):
    j = int(input())
        
    if coordinate >= 0:
        result = 0 - j
        paso = result
        coordinate += paso
    else:
        result = 0 + j
        paso = result
        coordinate += paso
    print(coordinate)

        
