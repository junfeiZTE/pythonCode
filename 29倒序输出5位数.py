x=int(input("Input a 5bit num:"))
a=x//10000
b=x%10000//1000
c=x%1000//100
d=x%100//10
e=x%10

if a:
    print('5bit',e,d,c,b,a)
elif b:
    print('4bit',e,d,c,b)
elif c:
    print('3bit',e,d,c)
elif d:
    print('2bit',e,d)
else:
    print('1bit',e)
