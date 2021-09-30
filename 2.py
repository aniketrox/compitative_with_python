num = str(input('Enter a four digit number: '))
summ=0
for i in range(0,4):
    dig = int(num[i])
    summ+=dig

print('the sum of the digits in your number: ',summ)
