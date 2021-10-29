m = int(input("How many numbers do yu want in your list: "))
a = []
for i in range(0,m):
    if i == 0:
        x = int(input("Enter your first number: "))
        a.append(x)
    else:
        x = int(input("Enter your next number: "))
        a.append(x)
       
def kk(a):
    r = len(a)
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if j == r-1:
                break
            elif a[j] >= a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
            else:
                continue
    coun_list = []
    sing_list = []
    large_list = []
    s = 0
    y = 0
    while s<r:
        ele = a[s]
        c = a.count(ele)
        y = ele
        coun_list.append(c)
        sing_list.append(y)
        s = s+c
    for i in range(0,len(sing_list)-1):
        if abs(sing_list[i]-sing_list[i+1])==1:
            h = coun_list[i]+coun_list[i+1]
            large_list.append(h)
        elif abs(sing_list[i]-sing_list[i+1])!=1:
            continue
    
    return max(large_list)

print("the length of the logest subarray is: ",kk(a))