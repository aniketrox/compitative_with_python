#write a program to input a 4 digit number and then it in the pattern decreasing pattern.

num = str(input('Enter a 4 digit number: '))
for i in range(0,4):
    print(num[0:4-i])
