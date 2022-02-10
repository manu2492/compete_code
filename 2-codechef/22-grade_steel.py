'''
Hardness of the steel must be greater than 50
Carbon content of the steel must be less than 0.7
Tensile strength must be greater than 5600
The grades awarded are as follows:

Grade is 10 if all three conditions are met
Grade is 9 if conditions (1) and (2) are met
Grade is 8 if conditions (2) and (3) are met
Grade is 7 if conditions (1) and (3) are met
Grade is 6 if only one condition is met
Grade is 5 if none of the three conditions are met
'''

t = int(input())
for _ in range(t):
    h,c,s = map(float, input().split())

    if h > 50 and c < 0.7 and s > 5600:
        print(10)
    elif h > 50 and c < 0.7:
        print(9)

    elif c < 0.7 and s > 5600:
        print(8)

    elif h > 50 and s > 5600:
        print(7)

    elif h > 50 or c < 0.7 or s > 5600:
        print(6)

    else:
        print(5)


