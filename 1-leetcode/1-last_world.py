'''
58. Length of Last Word
Given a string s consisting of some words separated by some number of spaces, return the length of the last
word in the string.

A word is a maximal substring consisting of non-space characters only.

 Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
'''
#solution 1

s = 'hello asdsa asdasf world'
s = s.split()
j = len(s)
word = s[j - 1]
print(len(word))

#better solution
#solution 2

n = 'hello asdsa asdasf world'

def last_word_solution(n):
    last_word = n.split()[-1]
    print(len(last_word))

last_word_solution(n)

