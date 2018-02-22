a=int(input("Input a 5bit num:"))

x=str(a)
flag=True

for i in range(int(len(x)/2)):
    if x[i] != x[-i-1]:
        flag=False
        break
if flag:
    print('%d huiwenshu'%a)
else:
    print('%d bushi huiwenshu'%a)
