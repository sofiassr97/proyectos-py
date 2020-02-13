'''
Problem 2
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

'''
s = 'azcbobobegghakl'
count = 0
for char in range(0, len(s)-2):
    if (s[char] == "b"):
        if (s[char + 1] == "o"):
            if (s[char + 2] == "b"):
                count += 1
                
print(count)             