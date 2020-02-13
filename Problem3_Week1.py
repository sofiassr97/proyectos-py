''' Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

'''
s = 'azcbobobegghakl' #este se debe de poner como input
a = ''
b = ''

for i in range(len(s)):
    a += s[i]
    if len(a) > len(b):
        b = a
    if i > len(s)-2:
        break
    if s[i] > s[i+1]:
        a = ''

print("Longest substring in alphabetical order is: {}".format(b))