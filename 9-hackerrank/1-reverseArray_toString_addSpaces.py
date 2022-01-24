# reverse array into a string array + spaces 

#given array
arr = [1,4,3,2]

#1-array reverse
arr = arr[::-1]

#2- create a empty string
strr = ''

#3- create a for loop
#this add items to a strr string and add a space
for i in arr:
   strr += ' ' + str(i)

#4-return the response
print(strr)
